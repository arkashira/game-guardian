import pytest
from src.config import Config, load_config, save_config
import json
import os

def test_config_from_dict():
    data = {"power_threshold": 75, "temperature_threshold": 85}
    config = Config.from_dict(data)
    assert config.power_threshold == 75
    assert config.temperature_threshold == 85

def test_config_to_dict():
    config = Config(power_threshold=75, temperature_threshold=85)
    data = config.to_dict()
    assert data["power_threshold"] == 75
    assert data["temperature_threshold"] == 85

def test_load_config():
    config = load_config()
    assert isinstance(config, Config)

def test_save_config(tmp_path):
    config = Config(power_threshold=75, temperature_threshold=85)
    save_config(config, tmp_path / "config.json")
    with open(tmp_path / "config.json", "r") as f:
        data = json.load(f)
    assert data["power_threshold"] == 75
    assert data["temperature_threshold"] == 85
