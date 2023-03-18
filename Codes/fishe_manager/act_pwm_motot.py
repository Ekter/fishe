#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import threading


class Servo:
    def __init__(self, angle_to_delay = None):
        self.angle = 0
        if angle_to_delay is None:
            self.angle_to_delay = lambda angle: 1.5 + 50/9000 * angle
        else:
            self.angle_to_delay = angle_to_delay
        self.attached = False
        self.t = threading.Thread(target=self.loop)
        self.t.start()

    def attach(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.attached = True

    def detach(self):
        self.attached = False
        GPIO.cleanup()

    def write(self, angle):
        if not self.attached:
            raise RuntimeError("Servo is not attached")
        if angle < -90 or angle > 90:
            raise ValueError("Angle must be between -90 and 90")
        self.angle = angle

    def loop(self):
        while True:
            if self.attached:
                t=time.time()
                GPIO.output(self.pin, GPIO.HIGH)
                while time.time()-t<=self.angle_to_delay(self.angle)/1000:
                    pass
                GPIO.output(self.pin, GPIO.LOW)
                while time.time()-t<=20/1000:
                    pass


def main():
    servo = Servo()
    servo.attach(12)
    while True:
        servo.write(37)
        time.sleep(0.011)
        servo.write(63)
        time.sleep(0.011)
        # ~1° de décalage en théorie

if __name__ == '__main__':
    main()
