import yaml
import sys
import json
import argparse
import re
import os
from common import constants

ANN_EMITS = 'emits'
ANN_DEFAULT = 'default'

C_METADATA = 'metadata'

IGNORE_LIST = ['apiVersion', 'kind']
DATA_TYPES = ['integer', 'string', 'array', 'boolean']
S2 = '  '
S1 = ' '
PLATFORMS = [constants.PLATFORM_SRL, constants.PLATFORM_SROS]
PRAGMA_NO_COVER = '  # pragma: no cover'

DUTS = ['dut1', 'dut2', 'dut3']
DUT_SPEC = {
    DUTS[0]: {
        "platform": "7220 IXR-D2L",
        "version": "23.10.2",
        "operatingSystem": constants.PLATFORM_SRL,
        "onBoarded": True
    },
    DUTS[1]: {
        "platform": "7220 IXR-D2L",
        "version": "24.3.2",
        "operatingSystem": constants.PLATFORM_SRL,
        "onBoarded": True
    },
    DUTS[2]: {
        "platform": "7750 SR-2se",
        "version": "23.7.3",
        "operatingSystem": constants.PLATFORM_SROS,
        "onBoarded": True
    },
}

DUT_CR_TEMPLATE = {
    "metadata": {
        "name": ""
    },
    "spec": {}
}


def parse_yaml_object(obj, name: str, class_map, ytags, sub_crds, is_root: bool, yenums):
    class_info = {}
    for key, value in obj.items():
        if is_root and key in IGNORE_LIST:
            print(f'ignoring {key}')
            continue
        ytags[key] = f'Y_{key.replace("-", "_").upper()}'
        prop_type = value['type']
        if prop_type == 'object':
            if key == 'metadata':
                class_info[key] = {'type': key.capitalize()}
            elif value.get('properties'):
                obj_prp = value.get('properties')
                desc = value.get('description', None)
                if desc and ANN_EMITS in desc:
                    sp1_str = f'[{ANN_EMITS}='
                    sp2_str = ']'
                    dparts = desc.split(sp1_str, 1)
                    if len(dparts) == 2:
                        e_value = dparts[1].split(sp2_str, 1)[0]
                        c_name = e_value
                        if c_name not in sub_crds:
                            sub_crds.append(c_name)
                            class_info[key] = {'type': c_name, ANN_EMITS: True}
                            parse_yaml_object(obj=value.get('properties'), name=c_name, class_map=class_map, ytags=ytags, sub_crds=sub_crds, is_root=True, yenums=yenums)
                    else:
                        print(f"Missing {ANN_EMITS} annotation for inner crd")
                        sys.exit(1)
                else:
                    c_name = f'{name}{key.capitalize()}'
                    class_info[key] = {'type': c_name}
                    parse_yaml_object(obj=value.get('properties'), name=c_name, class_map=class_map, ytags=ytags, sub_crds=sub_crds, is_root=False, yenums=yenums)
            else:
                c_name = f'{name}{key.capitalize()}'
                class_info[key] = {'type': c_name}
                class_map[c_name] = {}
        elif prop_type == 'array':
            class_info[key] = {'type': prop_type}
            subtype = value['items']['type']
            desc = value.get('description', None)
            class_info[key]['subtype'] = subtype
            if subtype == 'object':
                c_name = f'{name}{key.capitalize()}Item'
                class_info[key]['subtype'] = c_name
                if value['items'].get('properties'):
                    obj_prp = value['items'].get('properties')  # noqa
                    if desc and ANN_EMITS in desc:
                        sp1_str = f'[{ANN_EMITS}='
                        sp2_str = ']'
                        dparts = desc.split(sp1_str, 1)
                        if len(dparts) == 2:
                            e_value = dparts[1].split(sp2_str, 1)[0]
                            c_name = e_value
                            class_info[key]['subtype'] = c_name
                            class_info[key][ANN_EMITS] = True
                            if c_name not in sub_crds:
                                sub_crds.append(c_name)
                                parse_yaml_object(obj=value['items'].get('properties'), name=c_name, class_map=class_map, ytags=ytags, sub_crds=sub_crds, is_root=True, yenums=yenums)
                        else:
                            print(f"Missing {ANN_EMITS} annotation for inner crd")
                            sys.exit(1)
                    else:
                        parse_yaml_object(obj=value['items'].get('properties'), name=c_name, class_map=class_map, ytags=ytags, sub_crds=sub_crds, is_root=False, yenums=yenums)
                else:
                    class_map[c_name] = {}
            else:  # array of string
                # generate enums
                if value['items'].get('enum'):
                    print(f"Enum {name}:{key}:", value['items'].get('enum'))
                    for e in value['items'].get('enum'):
                        yenums[f'ENUM_{key.upper()}_{str(e).replace("-","_").replace(".","_").upper()}'] = e
        else:
            p_info = {'type': prop_type}
            class_info[key] = p_info
            desc = value.get('description', None)
            if desc is None:
                print(f"description missing for :{key}")

            default_val = value.get('default', None)
            # if default tag is not specified, check if default value is embedded in description.
            if default_val is None and desc is not None:
                sp1_str = f'[{ANN_DEFAULT}='
                sp2_str = ']'
                dparts = desc.split(sp1_str, 1)
                if len(dparts) == 2:
                    default_val = dparts[1].split(sp2_str, 1)[0]

            if default_val is not None:
                if prop_type == 'integer':
                    p_info[ANN_DEFAULT] = int(default_val)
                elif prop_type == 'boolean':
                    p_info[ANN_DEFAULT] = bool(default_val) if isinstance(default_val, bool) else default_val.capitalize()
                elif prop_type == 'string' and not any(re.findall(r'\'|\"', default_val)):
                    p_info[ANN_DEFAULT] = f'\"{default_val}\"'
                else:
                    p_info[ANN_DEFAULT] = default_val
            # add enum
            if value.get('enum', None) is not None:
                print(f"Enum {name}:{key}:", value.get('enum'))
                for e in value.get('enum'):
                    yenums[f'ENUM_{key.upper()}_{str(e).replace("-","_").replace(".","_").upper()}'] = e

    class_map[name] = class_info


def get_python_type(att_type, sub_type):
    if att_type == 'string':
        return 'str'
    elif att_type == 'integer':
        return 'int'
    elif att_type == 'boolean':
        return 'bool'
    elif att_type == 'array':
        return f'list[{get_python_type(sub_type, None)}]'
    else:
        return att_type


def _build_sub_cr(key, value, class_map, val_vars):
    # print("values: ", key, value)
    att_type = value['type']
    if att_type == 'Metadata':
        return {'name': f'val_{key}'}
    elif att_type not in DATA_TYPES:
        _ret_obj = {}
        sub_cr_class = class_map[att_type]
        for _key, _value in sub_cr_class.items():
            _ret_obj[_key] = _build_sub_cr(key + "_" + _key, _value, class_map, val_vars)
        return _ret_obj
    elif att_type == 'array':
        _ret_arr = []
        _ret_obj = {}
        attr_subtype = value.get('subtype')
        if attr_subtype not in DATA_TYPES:
            sub_cr_class = class_map[attr_subtype]
            for _key, _value in sub_cr_class.items():
                _ret_obj[_key] = _build_sub_cr(key + "_" + _key, _value, class_map, val_vars)
            _ret_arr.append(_ret_obj)
        else:
            val_vars.append(f'val_{key}')
            _ret_arr.append(f'val_{key}')
        return _ret_arr
    else:
        val_vars.append(f'val_{key}')
        return f'val_{key}'


def _add_test_process_cr(suffix, lines, rootname, val_vars, cr_obj):
    lines.append(f"\ndef test_process_cr_{suffix}():\n")
    lines.append(f"{S2*2}'''Sanity test for function process_cr'''")
    lines.append(f"\n{S2*2}val_metadata_name = 'test_{rootname.lower()}'")
    for v in val_vars:
        lines.append(f"\n{S2*2}{v} = 'abc'")
    lines.append(f"\n{S2*2}input_cr = ")
    lines.append(f"{json.dumps(cr_obj, indent=4)}\n")
    if CRD_TYPE == 'state':
        lines.append(f"{S2*2}{rootname.lower()}.process_state_cr(input_cr)\n")
    else:
        lines.append(f"{S2*2}{rootname.lower()}.process_cr(input_cr)\n")
    lines.append(f"{S2*2}assert len(eda.update_cr_list) == 1\n")
    lines.append(f"{S2*2}for cfg_cr in eda.update_cr_list:\n")
    lines.append(f"{S2*4}if cfg_cr['schema'] == schema.CONFIG_SCHEMA:\n")
    lines.append(f"{S2*6}assert cfg_cr['spec']['node-endpoint'] == DUT1\n")
    lines.append(f"{S2*6}'''add asserts here....'''\n")
    lines.append(f"{S2*4}elif cfg_cr['schema'] == schema.INTERFACE_STATE_SCHEMA:\n")
    lines.append(f"{S2*6}assert cfg_cr['spec']['members'][0]['node'] == DUT1\n")
    lines.append(f"{S2*6}'''add asserts here....'''\n\n")

    lines.append(f"{S2*2}for i in range(len(eda.update_cr_list)):\n")
    lines.append(f"{S2*4}eda.update_cr_list.pop(0)\n\n")
    lines.append(f"{S2*2}assert len(eda.update_cr_list) == 0\n")


def _generate_handlers(path, rootname: str, crd_import):
    handler_type = CRD_TYPE
    with open(f'{path}/{rootname.lower()}/handlers.py', 'w') as file:
        lines = ["#!/usr/bin/env python3\n"]
        lines.append('from common.constants import PLATFORM_SRL, PLATFORM_SROS, TAG_OS\n')
        for platform in PLATFORMS:
            lines.append(f'from .{platform} import {platform.capitalize()}Base{handler_type.capitalize()}Handler\n')

        lines.append(f"\n_{handler_type}_handlers = {{\n")

        lines.append(f"{S2*2}f'{{PLATFORM_SRL}}Base': {constants.PLATFORM_SRL.capitalize()}Base{handler_type.capitalize()}Handler(),\n")
        lines.append(f"{S2*2}f'{{PLATFORM_SROS}}Base': {constants.PLATFORM_SROS.capitalize()}Base{handler_type.capitalize()}Handler(),\n")
        lines.append("}\n\n")

        lines.append(f"\n\ndef get_{handler_type}_handler(node_cr):\n")
        lines.append(f"{S2*2}os = node_cr['spec'].get(TAG_OS)\n")
        lines.append(f"{S2*2}# version = node_cr['spec'].get('version')\n")
        lines.append(f"{S2*2}if os == PLATFORM_SROS:\n")
        lines.append(f"{S2*4}return _{handler_type}_handlers[f'{{PLATFORM_SROS}}Base']\n")
        lines.append(f"{S2*2}elif os == PLATFORM_SRL:\n")
        lines.append(f"{S2*4}return _{handler_type}_handlers[f'{{PLATFORM_SRL}}Base']\n")
        lines.append(f"{S2*2}return None{PRAGMA_NO_COVER}\n")
        file.writelines(lines)

    # """ generate template for eda handlers """
    with open(f'{path}/{rootname.lower()}/eda.py', 'w') as file:
        lines = [
            "#!/usr/bin/env python3\n",
            "# import eda_config as ecfg\n",
            "# import eda_common as eda\n",
            "# import utils.schema as s\n",
            "import os\n"
            "# import json\n",
            f"from {crd_import} import {rootname}\n\n"
            f"class EdaHandler:\n",
            f"{S2*2}def handle_cr(self, cr_obj: {rootname}):\n",
            f"{S2*4}# implement this\n",
            f"{S2*4}print('Eda handler is not implemented')\n"
        ]
        file.writelines(lines)

    # """ generate template for config handlers """
    for platform in PLATFORMS:
        with open(f'{path}/{rootname.lower()}/{platform}.py', 'w') as file:
            lines = [
                "#!/usr/bin/env python3\n",
                "# import eda_config as ecfg\n",
                "# import eda_common as eda\n",
                "# import utils.schema as s\n",
                "import os\n"
                "# import json\n",
                f"from {crd_import} import {rootname}\n\n"
                f"class {platform.capitalize()}Base{handler_type.capitalize()}Handler:\n",
                f"{S2*2}def handle_cr(self, cr_obj: {rootname}, node_cr=None):\n",
                f"{S2*4}# implement this\n",
                f"{S2*4}print('{platform.capitalize()} handler is not implemented')\n"
            ]
            file.writelines(lines)


def _generate_constants(path, rootname: str, ytags: map, yenums: map):
    with open(f'{path}/{rootname.lower()}/constants.py', 'w') as file:
        lines = [
            "#!/usr/bin/env python3\n",
            f"# constants for {rootname} crd\n\n",
        ]
        for key, value in ytags.items():
            lines.append(f"{value} = '{key}'\n")
        for key, value in yenums.items():
            lines.append(f"{key} = '{value}'\n")
        file.writelines(lines)


def _generate_classes(path, rootname: str, ytags: map, classes: map, sub_crds: list):
    with open(f'{path}/{rootname.lower()}/__init__.py', 'w') as file:
        lines = [
            "#!/usr/bin/env python3\n",
            f"# Module for support {rootname} crd\n\n",
            "from .constants import *\n",
            "from common.metadata import Metadata, Y_NAME\n"
        ]

        for key, value in classes.items():
            comment = ''
            if key == f'{rootname}Status':
                comment = PRAGMA_NO_COVER
            c_lines = [f'\n\nclass {key}:{comment}\n']
            if len(value) != 0:
                c_lines.append(f'{S2*2}def __init__(self,')
            constructor_attrs = []
            attrs_values_assignment = []

            method_to_input = [f'\n{S2*2}def to_input(self):{PRAGMA_NO_COVER}\n',
                               f'{S2*4}' + '_rval = {}\n']

            static_method = [f"\n{S2*2}@staticmethod\n",
                             f"{S2*2}def from_input(obj):\n",
                             f"{S2*4}if obj:\n"]

            static_method_return_stm = f"{S2*6}return {key}("
            for attr_name, att_val in value.items():
                att_type = att_val.get('type')
                attr_subtype = att_val.get('subtype')
                print_type = get_python_type(att_type, attr_subtype)

                # add metadata for inner crd as original crd will have metadata
                if key in sub_crds and attr_name == 'name':
                    constructor_attrs.append(f'\n{S2*4}{S1*9}metadata: Metadata,')
                    attrs_values_assignment.append(f'{S2*4}self.metadata = metadata\n')
                else:
                    constructor_attrs.append(f'\n{S2*4}{S1*9}{attr_name.replace("-","_")}: {print_type},')
                    attrs_values_assignment.append(f'{S2*4}self.{attr_name.replace("-","_")} = {attr_name.replace("-","_")}\n')

                if att_type not in DATA_TYPES:
                    if attr_name == C_METADATA:
                        static_method.append(f"{S2*6}_metadata = Metadata.from_input(obj.get(Y_METADATA)) if obj.get(Y_METADATA, None) else Metadata.from_name(obj.get(Y_NAME))\n")
                        method_to_input.append(f'{S2*4}if self.metadata is not None:\n')
                        method_to_input.append(f"{S2*6}_rval[Y_NAME] = self.metadata.name\n")
                    else:
                        static_method.append(f'{S2*6}_{attr_name.replace("-","_")} = {att_type}.from_input(obj.get({ytags[attr_name]}, None))\n')
                        method_to_input.append(f'{S2*4}if self.{attr_name.replace("-","_")} is not None:\n')
                        method_to_input.append(f'{S2*6}_rval[{ytags[attr_name]}] = self.{attr_name.replace("-","_")}.to_input()\n')

                elif att_type == 'array' and attr_subtype and attr_subtype not in DATA_TYPES:
                    # [Entry.from_dict(y) for y in obj.get("entries")]
                    static_method.append(f'{S2*6}_{attr_name.replace("-","_")} = [{attr_subtype}.from_input(y) for y in obj.get({ytags[attr_name]})] if obj.get({ytags[attr_name]}) else []\n')

                    method_to_input.append(f'{S2*4}if self.{attr_name.replace("-","_")} is not None:\n')
                    method_to_input.append(f'{S2*6}_rval[{ytags[attr_name]}] = [y.to_input() for y in self.{attr_name.replace("-","_")}]\n')

                elif key in sub_crds and attr_name == 'name':
                    static_method.append(f'{S2*6}_metadata = Metadata.from_input(obj.get(Y_METADATA)) if obj.get(Y_METADATA, None) else Metadata.from_name(obj.get(Y_NAME))\n')

                    method_to_input.append(f'{S2*4}if self.metadata is not None:\n')
                    method_to_input.append(f"{S2*6}_rval[Y_NAME] = self.metadata.name\n")

                else:
                    d_value = att_val.get('default', 'None')
                    static_method.append(f'{S2*6}_{attr_name.replace("-","_")} = obj.get({ytags[attr_name]}, {d_value})\n')

                    method_to_input.append(f'{S2*4}if self.{attr_name.replace("-","_")} is not None:\n')
                    method_to_input.append(f'{S2*6}_rval[{ytags[attr_name]}] = self.{attr_name.replace("-","_")}\n')

                if key in sub_crds and attr_name == 'name':
                    static_method_return_stm = static_method_return_stm + f"\n{S2*8}metadata=_metadata,"
                else:
                    static_method_return_stm = static_method_return_stm + f'\n{S2*8}{attr_name.replace("-","_")}=_{attr_name.replace("-","_")},'

            static_method.append(f"{static_method_return_stm})\n")
            static_method.append(f"{S2*4}return None{PRAGMA_NO_COVER}\n")
            method_to_input.append(f"{S2*4}return _rval\n")
            if len(value) != 0:
                constructor_attrs.append("):\n")

            lines = lines + c_lines + constructor_attrs + attrs_values_assignment + method_to_input + static_method
        file.writelines(lines)


def _generate_init_py(path, rootname: str, crd_import):
    """ init file """
    with open(f'{path}/{rootname.lower()}/init.py', 'w') as file:
        lines = [
            "#!/usr/bin/env python3\n\n",
            f"from {crd_import} import {rootname}\n"
            f"\ndef validate(cr: {rootname}):\n",
            f"{S2*2}# implement this\n",
            f"{S2*2}pass\n\n",
            f"\ndef init_globals_defaults(cr: {rootname}):\n",
            f"{S2*2}# implement this\n",
            f"{S2*2}pass\n",
        ]
        file.writelines(lines)


def _generate_intent_py(rootname: str, crd_import, subcrd_import):
    """ script file """
    handler_type = CRD_TYPE
    with open(f'{groupname}/{rootname.lower()}_intent.py', 'w') as file:
        lines = [
            "#!/usr/bin/env python3\n",
            f"# script to handle {rootname} cr\n",
            "import eda_config as ecfg\n",
            "import eda_common as eda\n"
            "import eda_state as estate\n"
            "import os\n"
            "import json\n"
            "import sys\n"
            "import utils.schema as s\n",
            "from utils.log import log_msg\n"
            f"from {crd_import} import {rootname}\n",
            f"from {subcrd_import}.init import validate, init_globals_defaults\n",
            f"from {subcrd_import}.handlers import get_{handler_type}_handler\n\n",
        ]
        if handler_type == 'config':
            lines.append("\ndef process_cr(cr):\n")
        else:
            lines.append("\ndef process_state_cr(cr):\n")

        lines = lines + [
            f"{S2*2}log_msg('{rootname} CR:', dict=cr)\n",
            f"{S2*2}cr_obj = {rootname}.from_input(cr)\n",
            f"{S2*2}validate(cr_obj)\n",
            f"{S2*2}init_globals_defaults(cr_obj)\n",
            f"{S2*2}# srl_handler = get_{handler_type}_handler('srlinux')\n",
            f"{S2*2}# srl_handler.handle_cr(cr_obj, node_cr)\n"
        ]
        file.writelines(lines)


def _generate_test_intent_py(rootname: str, classes: map,):
    """ test intent file """
    with open(f'{groupname}/test/test_{rootname.lower()}_intent.py', 'w') as file:
        lines = [
            "#!/usr/bin/env python3\n",
            f"# unit test for {rootname.lower()}_intent.py\n\n",
            # f"from common.{rootname.lower()}.constants import *\n",
            "import json\n",
            "import eda_config as ecfg\n",
            "import eda_common as eda\n"
            "import os\n"
            "from utils import schema\n",
            f'import {groupname}.{rootname.lower()}_intent as {rootname.lower()}\n\n'
        ]

        val_vars = []
        _cr_obj = {
            'apiVersion': f"{data['spec']['group']}/{data['spec']['versions'][0]['name']}",
            'kind': rootname,
            'metadata': {
                'name': 'val_metadata_name'
            }
        }

        _root_class = classes[rootname]
        _cr_obj['spec'] = _build_sub_cr('spec', _root_class['spec'], classes, val_vars)

        print('*****************************')
        print(f'*** CR var_vals *** \n {val_vars}')
        print(f'*** {rootname} CR *** \n {json.dumps(_cr_obj, indent=2)}')
        """add duts"""
        for d in DUTS:
            lines.append(f"\n{d.upper()} = '{d}'")
            DUT_CR_TEMPLATE['metadata']['name'] = d
            DUT_CR_TEMPLATE['spec'] = DUT_SPEC[d]
            lines.append(f"\n{d.upper()}_CR = ")
            lines.append(f"{json.dumps(DUT_CR_TEMPLATE, indent=4)}\n")

        # setup function
        lines.append("\ndef setup_module():\n")
        lines.append(f"{S2*2}'''Setup function'''\n")
        for d in DUTS:
            lines.append(f"{S2*2}ecfg.test_addcr(schema.TOPOLOGY_NODE_SCHEMA, {d.upper()}_CR)\n")
        lines.append(f"{S2*2}# add your code here\n")
        lines.append(f"{S2*2}# ecfg.test_add_alloc(....)\n\n")

        # teardown function
        lines.append("\ndef teardown_module():\n")
        lines.append(f"{S2*2}'''Teardown function'''\n")
        lines.append(f"{S2*2}ecfg.test_clear_all()\n\n")

        _add_test_process_cr("1", lines, rootname=rootname, val_vars=val_vars, cr_obj=_cr_obj)
        _add_test_process_cr("2", lines, rootname=rootname, val_vars=val_vars, cr_obj=_cr_obj)

        # main function
        lines.append('\nif __name__ == "__main__":\n')
        lines.append(f"{S2*2}setup_module()\n")
        lines.append(f"{S2*2}test_process_cr_1()\n")
        lines.append(f"{S2*2}test_process_cr_2()\n")
        lines.append(f"{S2*2}teardown_module()\n")

        # lines.append(f"print(json.dumps(INPUT_CR, indent=2))")

        file.writelines(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('crdfile', type=argparse.FileType('r'), help='CRD file')
    parser.add_argument('--crdtype', default='config', help='CRD type [state|config]')
    args = parser.parse_args()
    global CRD_TYPE
    CRD_TYPE = args.crdtype
    # Load YAML file
    with args.crdfile as file:
        data = yaml.safe_load(file)

    try:
        if data.get('kind') != 'CustomResourceDefinition':
            raise ValueError('input file should be of kind : CustomResourceDefinition')
        groupname = data['spec']['group'].split('.', 1)[0]
        rootname = data['spec']['names']['kind']
        properties = data['spec']['versions'][0]['schema']['openAPIV3Schema']['properties']
        CODE_GEN_PATH = f'{groupname}/pysrc'
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

    print(f"groupname: {groupname}, rootname: {rootname}")
    # build parent-child map for tags and subtags
    classes = {}
    ytags = {}
    yenums = {}
    sub_crds = []
    parse_yaml_object(obj=properties, name=rootname, class_map=classes, ytags=ytags, sub_crds=sub_crds, is_root=True, yenums=yenums)
    print(f'*** classes from yaml: *** \n {json.dumps(classes, indent=2)}')
    print(f'*** sub crds: *** \n {sub_crds}')

    if not os.path.exists(f'{CODE_GEN_PATH}/{rootname.lower()}'):
        os.makedirs(f'{CODE_GEN_PATH}/{rootname.lower()}')
    if not os.path.exists(f'{groupname}/test'):
        os.makedirs(f'{groupname}/test')

    # code generation
    crd_import = f'{groupname}.pysrc.{rootname.lower()}'
    subcrd_import = f'{groupname}.pysrc.{rootname.lower()}'
    _generate_constants(path=CODE_GEN_PATH, rootname=rootname, ytags=ytags, yenums=yenums)
    _generate_handlers(path=CODE_GEN_PATH, rootname=rootname, crd_import=crd_import)
    _generate_classes(path=CODE_GEN_PATH, rootname=rootname, ytags=ytags, classes=classes, sub_crds=sub_crds)
    _generate_init_py(path=CODE_GEN_PATH, rootname=rootname, crd_import=crd_import)
    _generate_intent_py(rootname=rootname, crd_import=crd_import, subcrd_import=subcrd_import)
    _generate_test_intent_py(rootname=rootname, classes=classes)

    for sub_crd in sub_crds:
        path = f'{CODE_GEN_PATH}/{rootname.lower()}'
        if not os.path.exists(f'{path}/{sub_crd.lower()}'):
            os.makedirs(f'{path}/{sub_crd.lower()}')
        crd_import = f'{groupname}.pysrc.{rootname.lower()}'
        subcrd_import = f'{groupname}.pysrc.{rootname.lower()}.{sub_crd.lower()}'
        _generate_handlers(path=path, rootname=sub_crd, crd_import=crd_import)
        _generate_init_py(path=path, rootname=sub_crd, crd_import=crd_import)
        _generate_intent_py(rootname=sub_crd, crd_import=crd_import, subcrd_import=subcrd_import)
        _generate_test_intent_py(rootname=sub_crd, classes=classes)
