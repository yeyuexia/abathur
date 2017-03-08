# coding: utf8

from .base_command import Command
from abathur.alias import AliasManager


class ListCommand(Command):
    def __init__(self):
        super().__init__("list", "list aliases")

    def add_custom_options(self, parser):
        pass

    def handle(self, args):
        aliases = AliasManager().get_all()
        for name, uri in aliases.items():
            print(f"{name}:  {uri}")
