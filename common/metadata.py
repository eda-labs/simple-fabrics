#!/usr/bin/env python3

Y_METADATA = 'metadata'
Y_NAME = 'name'
Y_LABELS = 'labels'
Y_NAMESPACE = 'namespace'


class Metadata:
    def __init__(self,
                 name: str,
                 namespace: str = None,
                 labels: dict = None):
        self.name = name
        self.namespace = namespace
        self.labels = labels

    def to_input(self):
        _rval = {}
        if self.name:
            _rval[Y_NAME] = self.name
        if self.name:
            _rval[Y_LABELS] = self.labels
        if self.namespace:
            _rval[Y_NAMESPACE] = self.namespace

    @staticmethod
    def from_yaml(obj):
        if obj:
            _name = obj.get(Y_NAME, None)
            _namespace = obj.get(Y_NAMESPACE, None)
            _labels = obj.get(Y_LABELS, None)
            return Metadata(
                name=_name,
                namespace=_namespace,
                labels=_labels,)
        return None

    @staticmethod
    def from_input(obj):
        if obj:
            _name = obj.get(Y_NAME, None)
            _namespace = obj.get(Y_NAMESPACE, None)
            _labels = obj.get(Y_LABELS, None)
            return Metadata(
                name=_name,
                namespace=_namespace,
                labels=_labels,)
        return None

    @staticmethod
    def from_name(_name: str):
        return Metadata(name=_name,)
