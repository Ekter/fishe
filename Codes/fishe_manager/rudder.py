#!/usr/bin/env python3
"""class rudder to manage the rudder of the fishe"""
import arduino_communicator

class Rudder:
    """class rudder to manage the rudder of the fishe"""
    def __init__(self, communicator : arduino_communicator.ArduinoCommunicator):
        self.communicator = communicator
        self.angle = 0
        self.min_angle = 90
        self.max_angle = -90

    def start(self):
        """start the rudder"""
        self.communicator.send(209)
        self.set_angle(0)

    def set_angle(self, angle : int):
        """set the angle of the rudder(between -90 and 90)"""
        if angle > self.max_angle:
            self.angle = self.max_angle
        elif angle < self.min_angle:
            self.angle = self.min_angle
        else:
            self.angle = angle
        self.communicator.send(int((self.angle+90)/6))

    def stop(self):
        """stop the rudder"""
        self.set_angle(0)
        self.communicator.send(220)

    def increase_angle(self, angle : int):
        """increase the angle of the rudder"""
        self.set_angle(self.angle + angle)

    def decrease_angle(self, angle : int):
        """decrease the angle of the rudder"""
        self.set_angle(self.angle - angle)
