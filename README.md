# Windscribe Auto IP Changer

## Overview

`windscribe_auto_ip_changer.py` is a Python script designed to automatically change your IP address using Windscribe VPN. The script connects to a randomly selected server from a predefined list of regions and waits for a specified amount of time before changing to a new server. This can be useful for maintaining privacy or circumventing geographic restrictions.

## Features

- **Automatic IP Rotation**: Connects to a random server from the list.
- **Customizable Wait Time**: You can set how long the script waits before changing the IP address.
- **Comprehensive Server List**: Includes a wide variety of global server locations.

## Prerequisites

- Python 3.x
- Windscribe CLI installed and configured on your system.

## Installation

1. **Install Python**: Ensure Python 3.x is installed on your system.
2. **Install Windscribe CLI**: Follow the [Windscribe CLI installation guide](https://windscribe.com/guides/cli) to set up the Windscribe command-line interface.
3. **Download the Script**: Clone this repository or download the `windscribe_auto_ip_changer.py` script to your local machine.

## Usage

1. **Modify the Script**:
    - Open `windscribe_auto_ip_changer.py` in a text editor.
    - Set your desired wait time by modifying the `timetowait` variable (in minutes).

    ```python
    timetowait = 5  # Change this value to set your custom wait time
    ```

2. **Run the Script**:
    - Open a terminal or command prompt.
    - Navigate to the directory where the script is located.
    - Run the script using the following command:

    ```bash
    python windscribe_auto_ip_changer.py
    ```

3. **Monitor the Output**:
    - The script will print the currently connected region, the connection time, and the wait time before changing the IP address.

## Configuration

- **Regions**: The script contains a list of server locations. You can modify the `regions` list in the script to add or remove servers as needed.

    ```python
    regions = [
        "Tirana - Besa", "Buenos Aires - Tango", "Adelaide - Lofty", 
        # Add more regions here
    ]
    ```

- **Wait Time**: Adjust the `timetowait` variable to set how long the script should wait between IP changes.

    ```python
    timetowait = 5  # in minutes
    ```

## Troubleshooting

- **Connection Issues**: Ensure that the Windscribe CLI is properly installed and configured. Test your connection manually using the Windscribe CLI command before running the script.
- **Script Errors**: Check for any syntax errors or missing dependencies in your Python environment.

## License

This script is provided as-is. Use it at your own risk. The author is not responsible for any issues that may arise from using this script.

## Contact

For any questions or issues, please open an issue on the [GitHub repository](#) or contact the author directly.

---

**Note:** The script requires the Windscribe CLI tool to be installed and properly configured on your system. Ensure you have set up your Windscribe account and have the CLI tool ready before running this script.
