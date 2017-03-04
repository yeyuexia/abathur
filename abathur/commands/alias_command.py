# coding: utf8

from .base_command import Command

from abathur.alias import AliasManager


class AliasCommand(Command):
    def __init__(slef):
        super().__init__("alias", "alias help")

    def add_custom_options(self, parser):
        parser.add_argument("alias",  help="")
        parser.add_argument("uri", help="")

    def handle(self, args):
        manager = AliasManager()
        manager.add(args.alias, args.uri)
