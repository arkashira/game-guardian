import argparse
import json
from dataclasses import dataclass
import platform
import os

@dataclass
class SystemMetrics:
    temperature: float
    power_usage: float

def get_system_metrics():
    if platform.system() == 'Linux':
        try:
            with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
                temperature = float(f.read()) / 1000
        except FileNotFoundError:
            temperature = 0.0
    else:
        temperature = 0.0
    power_usage = os.getloadavg()[0] * 100 / os.cpu_count()
    return SystemMetrics(temperature, power_usage)

def check_thresholds(metrics, threshold):
    if metrics.temperature > threshold or metrics.power_usage > threshold:
        return True
    return False

def send_alert(metrics, threshold):
    if check_thresholds(metrics, threshold):
        print(f"Alert: System temperature ({metrics.temperature}°C) or power usage ({metrics.power_usage}%) exceeds {threshold}% of maximum capacity")

def main():
    parser = argparse.ArgumentParser(description='Game Guardian')
    parser.add_argument('--threshold', type=int, default=90, help='Threshold percentage')
    args = parser.parse_args()
    metrics = get_system_metrics()
    print(f"System temperature: {metrics.temperature}°C, Power usage: {metrics.power_usage}%")
    send_alert(metrics, args.threshold)

if __name__ == "__main__":
    main()
