import pytest
from src.telemetry import get_telemetry_data, update_telemetry_data, display_telemetry_data, TelemetryData, TelemetryCollector

def test_get_telemetry_data() -> None:
    data = get_telemetry_data()
    assert data["power"] == 100.0
    assert data["temperature"] == 50.0
    assert data["voltage"] == 12.0

def test_update_telemetry_data() -> None:
    data = {"power": 150.0, "temperature": 60.0, "voltage": 15.0}
    update_telemetry_data(data)
    assert TelemetryCollector().data.power == 0.0  # collector is recreated
    collector = TelemetryCollector()
    update_telemetry_data(data)
    assert collector.data.power == 0.0  # collector is recreated

def test_update_telemetry_data_with_global_collector() -> None:
    data = {"power": 150.0, "temperature": 60.0, "voltage": 15.0}
    from src.telemetry import collector
    update_telemetry_data(data)
    assert collector.data.power == 150.0

def test_display_telemetry_data(capsys) -> None:
    data = {"power": 100.0, "temperature": 50.0, "voltage": 12.0}
    display_telemetry_data(data)
    captured = capsys.readouterr()
    assert "Power: 100.0, Temperature: 50.0, Voltage: 12.0" in captured.out

def test_telemetry_data_class() -> None:
    data = TelemetryData(100.0, 50.0, 12.0)
    assert data.power == 100.0
    assert data.temperature == 50.0
    assert data.voltage == 12.0
