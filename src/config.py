import json
from dataclasses import dataclass
import os

@dataclass
class Config:
    power_threshold: int
    temperature_threshold: int

    def to_dict(self):
        return {
            "power_threshold": self.power_threshold,
            "temperature_threshold": self.temperature_threshold
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            power_threshold=data["power_threshold"],
            temperature_threshold=data["temperature_threshold"]
        )

def load_config():
    app_data_folder = os.path.join(os.path.expanduser("~"), "AppData", "Local", "GameGuardian")
    config_file = os.path.join(app_data_folder, "config.json")
    if not os.path.exists(app_data_folder):
        os.makedirs(app_data_folder)
    if not os.path.exists(config_file):
        with open(config_file, "w") as f:
            json.dump({"power_threshold": 50, "temperature_threshold": 70}, f)
    with open(config_file, "r") as f:
        data = json.load(f)
    return Config.from_dict(data)

def save_config(config, path):
    with open(path, "w") as f:
        json.dump(config.to_dict(), f)
