#!/usr/bin/env python
"""class propeller to manage the propeller of the fishe"""

import RPi.GPIO as GPIO
import time

# Pin Definitions


def main():
    input_pin = 18  # BCM pin 18, BOARD pin 12
    # Pin Setup:
    GPIO.setmode(GPIO.BCM)  # BCM pin-numbering scheme from Raspberry Pi
    GPIO.setup(input_pin, GPIO.IN)  # set pin as an input pin
    
    print("Starting demo now! Press CTRL+C to exit")
    try:
        while True:
            value = GPIO.input(input_pin)
            # GPIO.output(input_pin,GPIO.LOW)
            print("Value read from pin {} : {}".format(input_pin,
                                                        value))
            time.sleep(1)
            input_pin+=1
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
