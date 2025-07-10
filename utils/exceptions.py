#!/usr/bin/env python3

class VersionError(Exception):
    def __init__(self, version_cr: str, version):
        self.version_cr = version_cr
        self.version = version
        self.message = f'version from cr ({self.version_cr}) does not match intent version ({self.version})'
        super().__init__(self.message)


class MissingDependency(Exception):
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.message = f'missing dependency of type {self.type} with name {self.name}'
        super().__init__(self.message)


class InvalidTelemetry(Exception):
    def __init__(self, path, message):
        self.path = path
        self.message = message
        self.message = f'invalid telemetry at path {self.path}: {self.message}'
        super().__init__(self.message)


class InvalidInput(Exception):
    pass


class MissingParameter(Exception):
    pass
