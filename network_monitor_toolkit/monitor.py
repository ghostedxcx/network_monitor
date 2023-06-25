import subprocess
import ping3
import time

import config


def check_network_connectivity(ip_address):
    try:
        response_time = ping3.ping(ip_address)
        if response_time is not None:
            print(f"Network connectivity to {ip_address} is OK. Response time: {response_time} ms")
        else:
            print(f"Network connectivity to {ip_address} is not available.")
    except subprocess.TimeoutExpired:
        print(f"Network connectivity to {ip_address} is not available.")


def monitor_network():
    while True:
      for ip_address in config.DEVICE_IPS:
        check_network_connectivity(ip_address)

        time.sleep(3)


if __name__ == "__main__":
    try:
      monitor_network()
    except KeyboardInterrupt:
       print("\nNetwork monitoring stopped.")

