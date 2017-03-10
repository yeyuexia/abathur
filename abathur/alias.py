# coding: utf8

import os
import re
import json
import uuid

from git import Repo
from monorequire import require

from .constant import (
    ALIAS_CONFIGURATION,
    LOCAL_RESOURCE,
    REMOTE_RESOURCE,
    REMOTE_RESOURCE_HEADER
)


class NotExistedAlias(Exception):
    def __init__(self, alias):
        self.alias = alias

    def __repr__(self):
        return f"not found alias name: {self.alias}"


class NotSupportException(Exception):
    def __init__(self, resource):
        self.resource = resource

    def __repr__(self):
        return f"not support the kind of resource: {self.resource}"


class AliasManager:
    def __init__(self):
        self._load_configuration()

    def _load_configuration(self):
        with require(ALIAS_CONFIGURATION) as f:
            src = f.read()
        self.aliases = self.load_alias(json.loads(src) if src else dict())

    def load_alias(self, json_file):
        return dict(
            [(alias, Alias(**source)) for alias, source in json_file.items()]
        )

    def add(self, name, uri):
        self.aliases[name] = self.generate_alias(uri)
        self._storage()

    def remove(self, name):
        if name not in self.aliases:
            raise NotExistedAlias(name)
        del self.aliases[name]
        self._storage()

    def get(self, name):
        if name not in self.aliases:
            raise NotExistedAlias(name)
        return self.aliases[name]

    def get_all(self):
        return dict([(name, alias.uri) for name, alias in self.aliases.items()])

    def _storage(self):
        caches = dict(
            (alias, value.to_dict()) for alias, value in self.aliases.items()
        )
        with require(ALIAS_CONFIGURATION, "w+") as f:
            json.dump(caches, f)

    def generate_alias(self, uri):
        return Alias(self.get_resource_type(uri), uri)

    @staticmethod
    def get_resource_type(resource):
        if os.path.exists(resource):
            return LOCAL_RESOURCE
        else:
            if any([re.match(re_string, resource) for re_string in REMOTE_RESOURCE_HEADER]):
                return REMOTE_RESOURCE
        raise NotSupportException(resource)


class Alias:
    def __init__(self, uri_type, uri):
        self.uri_type = uri_type
        self.uri = uri

    def to_dict(self):
        return dict(uri_type=self.uri_type, uri=self.uri)

    def fetch(self):
        if self.uri_type == REMOTE_RESOURCE:
            res = Repo.clone_from(self.uri, f"/tmp/abathur-{uuid.uuid1().hex}")
            return res.working_dir
        else:
            return self.uri
