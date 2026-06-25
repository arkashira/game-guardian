import pytest
from src.ui import UI
import os

def test_get_power_threshold():
    ui = UI()
    assert 50 <= ui.get_power_threshold() <= 100

def test_get_temperature_threshold():
    ui = UI()
    assert 70 <= ui.get_temperature_threshold() <= 100

def test_set_power_threshold():
    ui = UI()
    ui.set_power_threshold(75)
    assert ui.get_power_threshold() == 75

def test_set_temperature_threshold():
    ui = UI()
    ui.set_temperature_threshold(85)
    assert ui.get_temperature_threshold() == 85

def test_set_power_threshold_invalid():
    ui = UI()
    with pytest.raises(ValueError):
        ui.set_power_threshold(25)

def test_set_temperature_threshold_invalid():
    ui = UI()
    with pytest.raises(ValueError):
        ui.set_temperature_threshold(65)
