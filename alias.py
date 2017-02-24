# coding: utf8

import json
import uuid

from git import Repo

from resources import (
    require,
    get_resource_type,
    LOCAL_RESOURCE,
    REMOTE_RESOURCE
)


ALIAS_CONFIGURATION = "~/.abathur/alias.json"


class AliasManager:
    def __init__(self):
        self._load_configuration()

    def _load_configuration(self):
        with require(ALIAS_CONFIGURATION) as f:
            aliases = json.load(f)
        self.aliases = dict(
            [(alias, Alias(**source)) for alias, source in aliases]
        )

    def add(self, name, uri):
        self.alias[name] = self.generate_alias(uri)
        self._storage()

    def _storage(self):
        caches = dict(
            (alias, value.dumps()) for alias, value in self.aliases.items()
        )
        with require(ALIAS_CONFIGURATION) as f:
            json.dump(caches, f)

    def generate_alias(self, uri):
        return Alias(get_resource_type(uri), uri)


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
