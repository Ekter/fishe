#!/usr/bin/env python
"""Class for controlling a servo motor on the Jetson Nano."""
import time
import threading

from RPi import GPIO


class Servo:
    """Class for controlling a servo motor on the Jetson Nano.
    The servo is controlled by a PWM signal on a GPIO pin.
    Use degrees for the angle.

    use : `servo = Servo()\n
          servo.attach(12)\n
          servo.write(37)`
          """
    def __init__(self, angle_to_delay = None):
        self.angle = 0
        if angle_to_delay is None:
            self.angle_to_delay = lambda angle: 1.5 + 50/9000 * angle
        else:
            self.angle_to_delay = angle_to_delay
        self.attached = False
        self.pin = 0
        self.loop_thread = threading.Thread(target=self.__loop)
        self.loop_thread.start()

    def attach(self, pin):
        """Attach the servo motor to a GPIO pin."""
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.attached = True

    def detach(self):
        """Detach the servo motor from the GPIO pin."""
        self.attached = False
        GPIO.cleanup()

    def write(self, angle):
        """Set the angle of the servo motor. Angle in degrees."""
        if not self.attached:
            raise RuntimeError("Servo is not attached")
        if angle < -90 or angle > 90:
            raise ValueError("Angle must be between -90 and 90")
        self.angle = angle

    def __loop(self):
        """Loop function for the servo motor.
        DO NOT CALL DIRECTLY!!!!
        The __init__ does his work supposedly.
        """
        while True:
            if self.attached:
                beg_loop=time.time()
                GPIO.output(self.pin, GPIO.HIGH)
                while time.time()-beg_loop<=self.angle_to_delay(self.angle)/1000:
                    pass
                GPIO.output(self.pin, GPIO.LOW)
                while time.time()-beg_loop<=20/1000:
                    pass

    def __del__(self):
        self.detach()
        print("a")


def main():
    "main"
    servo = Servo()
    servo.attach(12)
    try:
        import random
        while True:
            servo.write(random.randint(-90, 90)
            time.sleep(1)
            # ~1° offset probably due to python's latency and my program
    except KeyboardInterrupt:
        del servo

if __name__ == '__main__':
    main()
