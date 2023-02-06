"""Program to read data from the probe and save it to a file. The probe is connected to the hotspot created by the Jetson Nano"""

import time
import os


def read_data_probe(ip_probe : str):
    with open(f"{ip_probe}:///home/probe/fishe/Codes/data_to_send.csv","r") as f:
        data = f.readline().strip()
        first_line = data
        if first_line == "Time,Temperature,Pressure,Humidity,Altitude":
            while data:
                data = f.readline().strip()
                if data:
                    print(data)
                    if len(data.split(","))!=5:
                        with open("data_from_probe.csv","a") as f2:
                            f2.write(data)
                