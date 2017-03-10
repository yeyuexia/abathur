# coding: utf8

from .base_command import Command
from abathur.alias import AliasManager


class RemoveCommand(Command):
    def __init__(self):
        super().__init__("remove", "remove alias")

    def add_custom_options(self, parser):
        parser.add_argument("alias", metavar="alias")

    def handle(self, args):
        AliasManager().remove(args.alias)
