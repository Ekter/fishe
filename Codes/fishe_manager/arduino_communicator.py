#!/usr/bin/env python


"""Module to communicate with the arduino"""

import time

import serial


class ArduinoCommunicator:
    """Class to communicate with the arduino"""
    def __init__(self, port='/dev/ttyUSB0', baudrate=115200, timeout=1):
        self.arduino = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        self.chars = "\r\n"

    def send(self, data):
        try:
            self.arduino.write(bytes([data]))
            print(f"sent : {bytes([data])}'")
        except:
            self.arduino.close()

    def send_trame(self, trame : list, delay=0.1):
        for data in trame:
            self.send(data)
            time.sleep(delay)
        self.clean()

    def read(self):
        try:
            data = self.arduino.readline()
            while data:
                print(f'->{data.decode().strip(self.chars)}<-')
                data = self.arduino.readline()
        except:
            self.arduino.close()

    def clean(self):
        try:
            self.arduino.reset_input_buffer()
            self.arduino.reset_output_buffer()
        except:
            self.arduino.close()
