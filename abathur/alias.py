# coding: utf8

import json
import uuid

from git import Repo
from monorequire import require

from .config import (
    ALIAS_CONFIGURATION,
    LOCAL_RESOURCE,
    REMOTE_RESOURCE,
    REMOTE_RESOURCE_HEADER
)


class NotExistedAlias(Exception):
    def __init__(self, alias):
        self.alias = alias


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
        self.alias[name] = self.generate_alias(uri)
        self._storage()

    def get(self, name):
        if name not in self.alias:
            raise NotExistedAlias(name)
        return self.alias[name]

    def _storage(self):
        caches = dict(
            (alias, value.dumps()) for alias, value in self.aliases.items()
        )
        with require(ALIAS_CONFIGURATION) as f:
            json.dump(caches, f)

    def generate_alias(self, uri):
        return Alias(get_resource_type(uri), uri)

    def get_resource_type(self, resource):
        if os.path.exists(resource):
            return LOCAL_RESOURCE
        elif resource.startswith(REMOTE_RESOURCE_HEADER):
            return REMOTE_RESOURCE
        raise NotSupportException()


class Alias:
    def __init__(self, uri_type, uri):
        self.uri_type = uri_type
        self.uri = uri

    def fetch(self):
        if self.url_type == REMOTE_RESOURCE:
            res = Repo.clone_from(self.uri, f"/tmp/abathur-{uuid.uuid1().hex}")
            return res.working_dir
        else:
            return self.uri
