# Fifteenth report -- 11/03/2022

This week, I modified the structure of the code of the raspberry pi pico to make it less prone to quit if a sensor disconects. To achieve that, I made the sensor connect each time a measure is asked. However, I chose to make the program raise exceptions if the sensor isn't found even after two attempts. I haven't found any "correct" and non-breaking way to do it, because if I just ignore the removed sensor, I would need to log a false measurement. 
I also started using the Jetson Nano GPIO, and it is sometimes strange. It says the Jetson Nano isn't a jetson card, and that it may bug.
It is also strange compared to arduino because the HIGH level is 3.3V, but it is like raspberry pi, so not a big change. It makes testing harder because I had to calculate the resistance...
