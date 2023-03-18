# Sixteenth report -- 13/03/2022

I tried to assemble the shell and the propeller with Nathan this week.
I screwed the bottom of the propeller in the shell, since Nathan designed a vertical part on the propeller specifically for that. It screwed it directly in the shell, so the plastic of the shell just got penetrated, and the screw got fixed with the expansive foam. It held very well, but I had put the propeller in the wrong direction, so I had to remove it. But the screws were stuck due to the moss's elasticity, so it was impossible to remove two of them. I had to cut a part of the shell... It's not very important, but it could cause vulnerabilities in the future. I'd prefer not having to print a new one, I'll do my best with this one...

Then I tried to activate PWM on the Jetson Nano to control the servo and brushless motors(We found a website explaining this several months ago, but it was not really necessary immediately)

Passive PWM is not enabled by default on the Jetson Nano, but, at least, one pin is PWM-capable(33 on board). However, it is also an analogic input pin, and is used so. So we need to change the jetson nano pin configuration to change pin 33 to be pwm. To do so, we need to replace the pin configuration file in the jetson nano settings, and to re-install the OS. But... we can't since Auvidea won't let us do so(the file we need to edit changes from one version of the jetson nano to another, and it also holds the jetson nano USB and HDMI pinout, so a wrong change could make the jetson nano unusable, and the usb on the auvidea JN30D isn't the same as the one on the nvidia jetson nano, so sending nvidia's file is highly risky, and we don't have auvidea's file).

So we can't do passive PWM, but we could try active PWM. I don't know if it is possible to hold precise frequencies...
Otherwise, we'll need to use an arduino board to control the servo and brushless motors, and to send the data to the jetson nano through the serial port. It's not a big deal, but it's a bit annoying.
