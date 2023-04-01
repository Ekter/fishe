#!/usr/bin/env python3
"""class propeller to manage the propeller of the fishe"""
import arduino_communicator

class Propeller:
    """class propeller to manage the propeller of the fishe"""
    def __init__(self, communicator : arduino_communicator.ArduinoCommunicator):
        self.communicator = communicator
        self.speed = 0
        self.max_speed = 30
        self.min_speed = -30

    def start(self):
        """start the propeller"""
        self.communicator.send(210)
        self.set_speed(0)

    def set_speed(self, speed : int):
        """set the speed of the propeller(between -30 and 30)"""
        if speed > self.max_speed:
            self.speed = self.max_speed
        elif speed < self.min_speed:
            self.speed = self.min_speed
        else:
            self.speed = speed
        self.communicator.send(self.speed+60-self.min_speed)

    def stop(self):
        """stop the propeller"""
        self.set_speed(0)
        self.communicator.send(220)

    def increase_speed(self, speed):
        """increase the speed of the propeller"""
        self.set_speed(self.speed + speed)

    def decrease_speed(self, speed):
        """decrease the speed of the propeller"""
        self.set_speed(self.speed - speed)
