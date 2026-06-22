import pytest
from unittest.mock import patch, MagicMock
from game_guardian import SystemMetrics, get_system_metrics, check_thresholds, send_alert
import os

@patch('os.getloadavg')
@patch('os.cpu_count')
def test_get_system_metrics(mock_cpu_count, mock_getloadavg):
    mock_getloadavg.return_value = (1, 2, 3)
    mock_cpu_count.return_value = 4
    metrics = get_system_metrics()
    assert isinstance(metrics, SystemMetrics)

def test_check_thresholds_below_threshold():
    metrics = SystemMetrics(temperature=80, power_usage=80)
    assert not check_thresholds(metrics, 90)

def test_check_thresholds_above_threshold():
    metrics = SystemMetrics(temperature=100, power_usage=80)
    assert check_thresholds(metrics, 90)

def test_send_alert_below_threshold(capsys):
    metrics = SystemMetrics(temperature=80, power_usage=80)
    send_alert(metrics, 90)
    captured = capsys.readouterr()
    assert "Alert:" not in captured.out

def test_send_alert_above_threshold(capsys):
    metrics = SystemMetrics(temperature=100, power_usage=80)
    send_alert(metrics, 90)
    captured = capsys.readouterr()
    assert "Alert:" in captured.out
