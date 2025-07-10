#
# Stub for EDA common, so you can run your scripts in bash
#
import os
import json
import sys

DEBUG = os.getenv('DEBUG') if os.getenv('DEBUG') is not None else False
gSpecDb = {}
update_cr_list = []


class Schema:
    def __init__(self, group, version, kind):
        self.group = group
        self.version = version
        self.kind = kind

    def __eq__(self, other):
        return self.group == other.group and self.version == other.version and self.kind == other.kind

    def __hash__(self):
        return hash(self.group) ^ hash(self.kind)

    def __reduce__(self):
        return (self.__class__, (self.group, self.version, self.kind))

    def __lt__(self, other):
        return f'{self.group}_{self.kind}_{self.version}' < f'{other.group}_{other.kind}_{other.version}'


def ec_log_msg(*msg, dict=None):  # pragma: no cover
    if DEBUG:
        if msg:
            print(*msg, sep='\n')
        if dict is not None:
            if sys.implementation.name == "micropython":
                print(json.dumps(dict))
            else:
                print(json.dumps(dict, indent=4))


def update_cr(schema, name, spec=None, status=None, labels: dict = {}, ns=None):
    global update_cr_list
    if labels != {}:
        cr: dict
        for cr in update_cr_list:
            if cr.get('schema', None) == schema and cr.get('name', None) == name:
                for k, v in labels.items():
                    cr[k] = v
                return
    temp_cr_dict = {}
    temp_cr_dict["schema"] = schema
    temp_cr_dict["name"] = name
    if spec is not None:
        temp_cr_dict["spec"] = spec
    if status is not None:
        temp_cr_dict["status"] = status
    if labels != {}:
        temp_cr_dict["labels"] = status
    update_cr_list.insert(0, temp_cr_dict)
    ec_log_msg(f'\n{schema.group}/{schema.version}/{schema.kind} name {name}:')
    if spec is not None:
        ec_log_msg("spec", dict=spec)
        ec_log_msg(f"================ configs for {name}")
        configs = spec.get('configs', [])
        for cfg in configs:
            ec_log_msg(cfg['path'], dict=json.loads(cfg['config']))
        ec_log_msg(f"================ done {name}")
    if status is not None:
        ec_log_msg(f"status: {status}")
    if labels is not None:
        ec_log_msg(f"labels: {labels}")

#
# Use this functions to add to a fake cr db
#


def test_addcr(schema, cr):
    global gSpecDb
    gvkDb = gSpecDb.get(schema, [])
    gvkDb.append(cr)
    gSpecDb[schema] = gvkDb
