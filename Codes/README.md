# Code

This folder is for those who want to know how it works. It contains the robot's code.
The code is organised in Platformio projects, each project is a folder containing the code and the configuration files.

--------------------------------------------------------------------

Ce dossier est pour ceux qui veulent savoir comment ça marche. Il contient le code du robot.
Le code est organisé en projets Platformio, chaque projet est un dossier contenant le code et les fichiers de configuration.



---
---
---
---
---
---
---
---
---
---
---
---

You can see an ancient communication project that could have been possible if we took a raspberry pi in the probe in [read_data_probe](read_data_probe.py), a code based on one-way communication via ftp acces to read the data files.

But we couldn't do it because the raspberry py doesn't have any analog input pin, so it can't read ph, nor use the analog temperature sensor.

[sensors with analog inputs](Test/cours2/src/)
Here are my example codes for arduino to use the sensors.

[test pico](raspberry_pi_pico/) is the folder where I put my tests on the raspberry pi pico. The current program is a web server hosted on the pico, that can be accessed by a browser on the same network. I won't use it as it is, since I will make the server run on the Jetson nano(next paragraph), but it is a good example of how to use the pico as a web server and manage his connexions.

[Jetson nano web server](fishe_server/) is the folder where I put my web server for the Jetson Nano, built with Django. It is quite simple to use, just create a venve, install the requirements, and run the server.
It supports data insterting in the database via POST and GET requests, so I will use it easily to send data from the probe to the server.

[Jetson nano partitionning problems](../Reports/Reports_Nino_Mulac/Nano_partitionning.md) is a file where I explained all the problems with the Jetson Nano's storage, and how I managed to solve them.

