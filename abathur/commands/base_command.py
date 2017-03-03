# coding: utf8


class Command:
    def __init__(self, name, helper):
        self.name = name
        self.helper = helper

    def add_options(self, parser):
        self.add_custom_options(parser)

    def inject(self, parser):
        sub_parser = parser.add_parser(self.name, help=self.helper)
        self.add_options(sub_parser)
        sub_parser.set_defaults(handle=self.handle)

    def handle(self, args):
        raise NotImplementedError(f"sub-command {self.name} function not implemention")
