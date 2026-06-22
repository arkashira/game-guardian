import time
import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class TelemetryData:
    power: float
    temperature: float
    voltage: float

class TelemetryCollector:
    def __init__(self):
        self.data = TelemetryData(0.0, 0.0, 0.0)

    def collect_data(self) -> TelemetryData:
        # Simulate collecting data
        self.data.power = 100.0
        self.data.temperature = 50.0
        self.data.voltage = 12.0
        return self.data

    def update_data(self, data: TelemetryData) -> None:
        self.data = data

class TelemetryDisplay:
    def __init__(self):
        self.data = TelemetryData(0.0, 0.0, 0.0)

    def display_data(self, data: TelemetryData) -> None:
        print(f"Power: {data.power}, Temperature: {data.temperature}, Voltage: {data.voltage}")

collector = TelemetryCollector()
display = TelemetryDisplay()

def get_telemetry_data() -> Dict:
    data = collector.collect_data()
    return {
        "power": data.power,
        "temperature": data.temperature,
        "voltage": data.voltage
    }

def update_telemetry_data(data: Dict) -> None:
    telemetry_data = TelemetryData(data["power"], data["temperature"], data["voltage"])
    collector.update_data(telemetry_data)

def display_telemetry_data(data: Dict) -> None:
    telemetry_data = TelemetryData(data["power"], data["temperature"], data["voltage"])
    display.display_data(telemetry_data)

def main() -> None:
    while True:
        data = get_telemetry_data()
        display_telemetry_data(data)
        time.sleep(5)

if __name__ == "__main__":
    main()
