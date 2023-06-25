Network Monitoring Toolkit
The Network Monitoring Toolkit is a Python-based tool that allows you to monitor network connectivity, device status, and perform basic diagnostics. This tool utilizes ICMP ping checks to determine network reachability and response times. It provides a simple and straightforward way to keep track of your network's health.


Prerequisites
Before using the Network Monitoring Toolkit, ensure that you have the following prerequisites installed:

Python 3.x: You can download Python from the official Python website: https://www.python.org/downloads/

Getting Started

Clone the repository or download the source code files to your local machine.

Install the required Python libraries. Open a terminal or command prompt and navigate to the project's directory. Run the following command:

pip install ping3

Update the config.py file with the IP addresses of the devices you want to monitor. Modify the DEVICE_IPS list to include the IP addresses of the devices.

DEVICE_IPS = ["192.168.0.1", "192.168.0.2"]

Run the Network Monitoring Toolkit. Open a terminal or command prompt, navigate to the project's directory, and run the following command:

python monitor.py

The tool will start monitoring the network connectivity and device status based on the specified IP addresses. It will display the results in the console window.


To stop the network monitoring, press Ctrl+C in the terminal or command prompt. The program will catch the KeyboardInterrupt exception and print a message indicating that the network monitoring has stopped.

Customize and expand the tool as needed. You can modify the check_network_connectivity function in the monitor.py file to add additional monitoring checks or implement more advanced diagnostics.


Configuration

The Network Monitoring Toolkit provides a configuration file config.py to manage the IP addresses of the devices to monitor. Modify this file to update the IP addresses according to your network setup.

DEVICE_IPS = ["192.168.0.1", "192.168.0.2"]

Contributing
Contributions to the Network Monitoring Toolkit are welcome! If you have any ideas, improvements, or bug fixes, feel free to submit a pull request.