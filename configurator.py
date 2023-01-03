from configparser import ConfigParser
from easydict import EasyDict as edict
import logging

config = edict()

def make_config(config):
    parser = ConfigParser()
    parser.read(config)

    if not parser.sections():
        return False

    for section in parser.sections():
        config[section] = edict()

        for key, value in parser.items(section):
            config[section][key] = value

    return True