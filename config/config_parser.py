import os

import configparser

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class ConfigParser:
    def __init__(self, path):
        self.config = configparser.ConfigParser()
        self.config.read(f'{ROOT_DIR}{path}')
