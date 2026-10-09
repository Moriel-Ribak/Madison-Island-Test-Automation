import configparser
import json
from pathlib import Path


class ConfigReader:

    @staticmethod
    def read_config(section, key):
        root_dir = Path(__file__).resolve().parent.parent
        config_path = root_dir / "config.ini"

        print("config path:", config_path)

        config = configparser.ConfigParser()
        config.read(config_path)

        print("sections:", config.sections())

        if config.has_section(section) and config.has_option(section, key):
            return config[section][key]

        raise KeyError(
            f"Section '{section}' or key '{key}' not found in {config_path}"
        )

    @staticmethod
    def read_list(section, key):
        value = ConfigReader.read_config(section, key)
        return json.loads(value)