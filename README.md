<h3 align="center">🛠️ Game Guardian</h3>

<div align="center">
  <a href="https://github.com/axentx/game-guardian/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
  <a href="https://github.com/axentx/game-guardian">
    <img src="https://img.shields.io/badge/Language-Python-blue.svg" alt="Language: Python">
  </a>
  <a href="https://github.com/axentx/game-guardian/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/axentx/game-guardian/build.yml?branch=main" alt="Build Status">
  </a>
  <a href="https://github.com/axentx/game-guardian/stargazers">
    <img src="https://img.shields.io/github/stars/axentx/game-guardian?style=social" alt="Stars">
  </a>
</div>

---
# 🚀 Game Guardian
**Power system administrators with real-time telemetry data.** Game Guardian is a simple telemetry system that collects and displays real-time data on system power, temperature, and voltage.

## Why Game Guardian?
* **Real-time Data**: Collects and displays real-time data on system power, temperature, and voltage.
* **Easy to Use**: Designed to be run using the main.py file and includes testing capabilities using pytest.
* **Flexible**: Built using Python and utilizes the poetry build system.
* **Modular**: The system's functionality is contained within the src.telemetry module, which is imported and executed in the main.py file.
* **Tested**: Includes testing capabilities using pytest.
* **Documented**: Includes startup artifacts such as PRD.md, REQUIREMENTS.md, TECH_SPEC.md, BMC.md, STORIES.md, and ROADMAP.md.

## Feature Overview
| Feature | Description |
| --- | --- |
| Real-time Data Collection | Collects and displays real-time data on system power, temperature, and voltage. |
| Testing Capabilities | Includes testing capabilities using pytest. |
| Modular Design | The system's functionality is contained within the src.telemetry module. |

## Tech Stack
* Python
* Poetry
* Pytest

## Project Structure
* business: Business-related files
* docs: Documentation files
* src: Source code files
* tests: Test files
* main.py: Entry point of the application
* pyproject.toml: Poetry configuration file
* README.md: This file

## Getting Started
To get started with Game Guardian, follow these steps:
```bash
# Clone the repository
git clone https://github.com/axentx/game-guardian.git

# Navigate to the repository
cd game-guardian

# Install the dependencies
poetry install

# Run the application
poetry run python main.py

# Run the tests
poetry run pytest
```

## Deploy
To deploy Game Guardian, follow these steps:
```bash
# Build the application
poetry build

# Deploy the application
# TODO: Add deployment instructions
```

## Status
Game Guardian is currently in the early stage of development. The most recent commit was 9e5b202, which updated the documentation.

## Contributing
To contribute to Game Guardian, please see [CONTRIBUTING.md](CONTRIBUTING.md).

## License
Game Guardian is licensed under the MIT License. See [LICENSE](LICENSE) for more information.