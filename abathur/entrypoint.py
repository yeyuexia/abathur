# coding: utf8

import argparse

from abathur import Builder

DESCRIPTION = """
Abathur help you build project based on template.
"""
DEFAULT_TEMPLATE_PATH = "template"


def generate_argument_parser():
    parser = argparse.ArgumentParser(
        prog="abathur", description=DESCRIPTION
    )
    parser.add_argument("command", required=True)
    parser.add_argument("args", nargs="*")


if __name__ == "__main__":
    args = generate_argument_parser().parse_args()

    template_path = args.template or DEFAULT_TEMPLATE_PATH
    dest_root = args.output or args.project_name
    Builder(
        args.project_name, template_path, dest_root,
        args.placeholder, args.file
    ).build()
