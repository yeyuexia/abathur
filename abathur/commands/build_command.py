# coding: utf8

from .base_command import Command
from abathur.abathur import build


class BuildCommand(Command):
    def __init__(self):
        super().__init__("build", "build project based on template")

    def add_custom_options(self, parser):
        parser.add_argument("--alias", "-a", metavar="alias", required=True)
        parser.add_argument(
            "project_name", metavar="project_name"
        )
        parser.add_argument("--config", "-f", metavar="config")
        parser.add_argument("--output", "-o", metavar="output path")

    def handle(self, args):
        return build(
            args.project_name,
            args.output if args.output else args.project_name,
            args.alias,
            args.config
        )
