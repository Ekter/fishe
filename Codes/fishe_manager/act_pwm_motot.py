#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import threading


class Servo:
    def __init__(self):
        self.angle = 0
        self.angle_to_delay = lambda angle: 1500 + 50/9 * angle
        self.attached = False
        t = threading.Thread(target=self.loop)
        t.start()

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
        servo.write(90)
        time.sleep(1)
        servo.write(-90)
        time.sleep(1)

if __name__ == '__main__':
    main()