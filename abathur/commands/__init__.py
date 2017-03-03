# coding: utf8

from argparse import ArgumentParser

from .alias_command import AliasCommand
from .build_command import BuildCommand


DESCRIPTION = """
Abathur help you build project based on template.
"""


def get_parser():
    parser = ArgumentParser(description=DESCRIPTION)
    subparser = parser.add_subparsers()
    AliasCommand().inject(subparser)
    BuildCommand().inject(subparser)
    return parser
