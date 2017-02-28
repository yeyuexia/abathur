# coding: utf8

import os.path

from .alias import AliasManager
from .builder import TemplateBuilder

ABATHUR_CONFIGURATION = ".abathur"


def get_abathur_config(template_path):
    config = os.path.join(template_path, ABATHUR_CONFIGURATION)
    if not (os.path.exists(config) and os.path.isfile(config)):
        return list()
    with open(config, "r") as f:
        return ["{" + name.strip() + "}" for name in f.readlines()]


def process_configuration(template_path, custom_config, project_name):
    placeholders = get_abathur_config(template_path)
    config = dict()
    config["{PROJECT_NAME}"] = project_name
    for placeholder in placeholders:
        if placeholder in custom_config:
            print(f"load value {custom_config[placeholder]} for {placeholder}")
            config[placeholder] = custom_config[placeholder]
        else:
            config[placeholder] = input(f"please input value of placeholder `{placeholder}`:")
    return config


def read_custom_config(config):
    def parse_placeholder(src):
        key, value = src.split("=")
        return "{" + key.strip() + "}", value.strip()
    if not config:
        return dict()
    with open(config, "r") as f:
        return dict([parse_placeholder(source) for source in f.readlines()])


def build(project_name, target, alias, custom_config):
    temp = AliasManager().get(alias).fetch()
    config = process_configuration(
        temp, read_custom_config(custom_config), project_name
    )
    TemplateBuilder(project, temp, target, config).build()

