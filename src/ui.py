import os
from src.config import load_config, save_config

class UI:
    def __init__(self):
        self.config = load_config()

    def get_power_threshold(self):
        return self.config.power_threshold

    def get_temperature_threshold(self):
        return self.config.temperature_threshold

    def set_power_threshold(self, value):
        if 50 <= value <= 100:
            self.config.power_threshold = value
            config_path = os.path.join(
                os.path.expanduser("~"),
                "AppData",
                "Local",
                "GameGuardian",
                "config.json"
            )
            save_config(self.config, config_path)
        else:
            raise ValueError("Power threshold must be between 50 and 100")

    def set_temperature_threshold(self, value):
        if 70 <= value <= 100:
            self.config.temperature_threshold = value
            config_path = os.path.join(
                os.path.expanduser("~"),
                "AppData",
                "Local",
                "GameGuardian",
                "config.json"
            )
            save_config(self.config, config_path)
        else:
            raise ValueError("Temperature threshold must be between 70 and 100")
