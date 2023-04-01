# Eighteenth report -- 28/03/2022

This week, I modified my arduino enslavement program to allow the control of two servos.
This way, I can control the rudder(with the servo motor) and the propeller(with the ESC, commanded as a servo).

I had to change the way the data is spread between 0 and 255 to allow the control of two servos.
Since I need to send data between 0 and 180 for the servos, I chose to divide it by 6, making the data between 0 and 30.
This way, I can use multiple servos, but the precision isn't very good.
However, the ESC doesn't have a linear speed distribution, if fact, all its speed range can be found making the servo angle vary from 60 to 120, so I made a second range of control for the ESC.

This way, I can control the first servo between 0 and 180° with a precision of 6° between 0 and 30 of my data, the ESC as a servo the same way between 30 and 60, and the ESC directly between 60 and 120 between this values of my data.
Then I have 209 to attach the servo motor to pin 9, 210 to attach the ESC to pin 10, 219 to detach the servo motor, and 220 to detach the ESC.

With this new version of the program, I lose the option of changing the pin, as they are now hard-coded in the program, but I can control two servos, and I can control the ESC directly.

I tried the whole programmed, and it worked.


I made a bash program to launch the fishe(both the movement controller using the arduino and the web server for data transfer) [here](../../Codes/fishe_manager/runfishe.sh).
It launches both python programs simultaneously, the server on a virtual environment, and the movement manager on the system python, because I couldn't make it work on the virtual environment, the serial module seems not to be installable on it.

It seems to work, but I didn't manage to stop the ESC when I sent the command for a speed of 0, and I don't know why.

