import argparse
from pprint import pprint
from time import sleep

import matplotlib.pyplot
import matplotlib.pyplot as plt

import requests

parser = argparse.ArgumentParser(description="Mathplot status")
parser.add_argument("--hostname", default="192.168.1.1", help="Name of the host name")
args = parser.parse_args()
hostname = str(args.hostname)


def get_host_status():
    global hostname

    response = requests.get("http://127.0.0.1:5000/hosts/status")
    if response.status_code != 200:
        print(f"get hosts failed: {response.reason}")
        return {}

    return response.json()


def main():

    while True:
        status = get_host_status()
        status_list = status["status"]
        availability_array = list()
        time_array = list()
        for item in status_list:
            for key, value in item.items():
                if key == "availability":
                    if not value:
                        availability_array.append(0)
                    else:
                        availability_array.append(1)
                if key == "time":
                    time_array.append(value[11:16])

        plt.plot(time_array, availability_array)
        plt.show()
        matplotlib.pyplot.close("all")
        sleep(4)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bye!")
        exit()
