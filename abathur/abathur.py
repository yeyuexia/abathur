# coding: utf8

import os.path

from .alias import AliasManager
from .builder import TemplateBuilder
from .constant import (
    ABATHUR_CONFIGURATION,
    ABATHUR_CONFIGURATION_ROOT,
    IGNORE_FILES
)

def prepare_environment():
    if not os.path.exists(ABATHUR_CONFIGURATION_ROOT):
        os.mkdir(ABATHUR_CONFIGURATION_ROOT)

def get_abathur_config(template_path):
    config = os.path.join(template_path, ABATHUR_CONFIGURATION)
    if not (os.path.exists(config) and os.path.isfile(config)):
        return list()
    with open(config, "r") as f:
        return ["{" + name.strip() + "}" for name in f.readlines() if name.strip()]


def process_configuration(template_path, custom_config, project_name):
    placeholders = get_abathur_config(template_path)
    config = dict()
    project_name_value = input(f"please input value of placeholder `{'PROJECT_NAME'}`(default {project_name}:").strip()
    config["{PROJECT_NAME}"] = project_name_value if project_name_value else project_name
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
    TemplateBuilder(project_name, temp, target, config, IGNORE_FILES).build()

