import eda_config as ecfg
import utils.schema as s
from utils.log import log_msg

INCLUDE_DEFAULT = True
INCLUDE_BASE = True


def get_node(name: str, ns: str = None):
    node_cr = ecfg.get_cr(
        schema=s.TOPOLOGY_NODE_SCHEMA,
        name=name,
        ns=ns)
    if node_cr is not None and node_cr['spec'].get('onBoarded', False):
        return node_cr
    if node_cr is not None:  # pragma: no cover
        log_msg(f'get_node: node "{name}" is not onBoarded')
    return None


def list_nodes_all_namespaces(filter=[], label_filter=[]):
    namespace_onboarded_nodes = {}
    for namespace in ecfg.list_crs(schema=s.NAMESPACE_SCHEMA, filter=filter, label_filter=label_filter):
        namespace_name = namespace['metadata']['name']
        namespace_onboarded_nodes[namespace_name] = {}
        for toponode_cr in ecfg.list_crs(ns=namespace_name, schema=s.TOPOLOGY_NODE_SCHEMA, filter=filter, label_filter=label_filter):
            if toponode_cr['spec'].get('onBoarded', False):
                namespace_onboarded_nodes[namespace_name][toponode_cr['metadata']['name']] = toponode_cr
            node_name = toponode_cr['metadata']['name']
            log_msg(f'list_nodes_all_namespaces: node "{node_name}" is not onboarded, skipping it')
    if INCLUDE_BASE:
        namespace_onboarded_nodes['_base_'] = {}
        for toponode_cr in ecfg.list_crs(ns='_base_', schema=s.TOPOLOGY_NODE_SCHEMA, filter=[], label_filter=[]):
            if toponode_cr['spec'].get('onBoarded', False):
                namespace_onboarded_nodes['_base_'][toponode_cr['metadata']['name']] = toponode_cr
    if INCLUDE_DEFAULT:
        namespace_onboarded_nodes['default'] = {}
        for toponode_cr in ecfg.list_crs(ns='default', schema=s.TOPOLOGY_NODE_SCHEMA, filter=[], label_filter=[]):
            if toponode_cr['spec'].get('onBoarded', False):
                namespace_onboarded_nodes['default'][toponode_cr['metadata']['name']] = toponode_cr
    return namespace_onboarded_nodes


def list_nodes(filter=[], label_filter=[], ns=None):
    onBoarded_nodes = []
    for toponode_cr in ecfg.list_crs(schema=s.TOPOLOGY_NODE_SCHEMA, filter=filter, label_filter=label_filter, ns=ns):
        if toponode_cr['spec'].get('onBoarded', False):
            onBoarded_nodes.append(toponode_cr)
        node_name = toponode_cr['metadata']['name']
        log_msg(f'list_nodes: node "{node_name}" is not onBoarded, skipping it')
    return onBoarded_nodes
