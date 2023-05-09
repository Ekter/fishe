#!/usr/bin/env python3
"""class probe_manager to manage the probe of the fishe"""
import arduino_communicator

class ProbeManager:
    """class probe_manager to manage the probe of the fishe"""
    def __init__(self, communicator : arduino_communicator.ArduinoCommunicator):
        self.communicator = communicator
        self.way = 0

    def start(self):
        """start the probe?"""
        self.communicator.send(211)
        self.stop()

    def stop(self):
        """stop the probe from moving"""
        self.communicator.send(221)

    def go_up(self):
        """makes the probe go up"""
        self.communicator.send(121)

    def go_down(self):
        """makes the probe go down"""
        self.communicator.send(122)
