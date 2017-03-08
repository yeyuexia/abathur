# coding: utf8

from .base_command import Command

from abathur.alias import AliasManager


class AddCommand(Command):
    uri_helper = (
            "template uri, template can be "
            "a local resource or remote git repository"
    )

    def __init__(slef):
        super().__init__("add", "add alias for indicate template")

    def add_custom_options(self, parser):
        parser.add_argument("name",  help="alias name")
        parser.add_argument("uri", help=self.uri_helper)

    def handle(self, args):
        manager = AliasManager()
        manager.add(args.name, args.uri)
