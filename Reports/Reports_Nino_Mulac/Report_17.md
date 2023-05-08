# Seventeenth report -- 21/03/2023


This week, I tried to use my PWM program, as detailed in the previous report.
The first problem I was confronted to was the lack of current the Jetson Nano can provide : it could make my little servo at home(not a 9g, a standard black one) work, but when I tried using the 25kg/cm servo we need for the fishe, the jetson nano shut down immediately : its power supply wasn't powerful enough, or maybe the jetson nano gpio limits the drawn current.
So I needed to use an external generator.
After changing the power supply, I tried again, and it worked, but only at stable orders : if I asked the servo to go to -60° then to 45° after one second, it executes it pretty well.
However, for a sweeping command, making the angle go from -60° to 45° in 1°/0.1s, the effective angle was around the correct one, but it shakes a lot, and the servo is not stable.
To make it more stable, I should lower the frequency(to increase the period), but I am currently at 50Hz, and it is the standard minimum for servos.
So my program could work for a servo and not for another if I changed that...
I could also modify my program in some ways : firstly by just optimizing it, since it currently computes the time each time it checks if it is time to change the output, and secondly, by using timed functions that activate on precise times.

Another way of controlling the servo is to use a arduino as a bridge.
I made a program to connect to an arduino with usb from the jetson nano [here](../../Codes/fishe_manager/arduino_communication.py).

[Here](../../Codes/fishe_manager/pwm_control_nano_arduino/src/main.cpp) is the arduino program to read the serial signal from the jetson nano, and convert it to servo instructions.

It works using data packets as an unsigned int from 8 bits, so 1 byte, to make it easier to send and receive.

If this number is between 0 and 180, it is an angle, and the servo will go to this angle.

If it is between 181 and 200, it is an attach command, and the servo will attach to the pin (181-number).
For example, if the number is 190, the servo will attach to pin 9.

If it is 201, it is a detach command, and the servo will detach.



I tried this program, and it worked as long as I didn't plug my black servo motor on the arduino.
It is strange, since the arduino is powered by the jetson nano, the servo is powered by the arduino, and it worked previously when the servo was directly on the jetson nano.
It seems the arduino draws too much current...
I'll try to use it with a power supply during the courses.

Another problem is that the connection seems to need 5s approximately to be functional, but I don't know why.
It is not a big problem, but it is annoying, especially when trying to find out wether the arduino is connected or not.
