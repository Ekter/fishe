# Eight report -- 14/12/2022

Task according to the Gantt chart :

* Simples designs impression + assembly

I have set up the Nvidia Jetson Nano to use it as a ssh server, even when not connected to the computer by a wire.
Because of the debug purpose of the jetson nano, Nvidia decided to allow us to use it as a ssh server by creating a virtual network interface over an USB-C serial connection.
It is very useful, but when we'll use the fishe, we won't be able to plug it to a computer...
We probably won't be able to connect it to internet anyway, but that's another problem.

## Wifi connection

So the first step is to make the Jetson Nano connect to a wifi network.
*I made this with Maximilien, from the snoop team*

Without graphical interface, the normal way to do it is to manually edit configuration files, adding the wifi network's SSID and password, then to create a connection to it, to receive the IP address and so on.

This task is very hard, because the Jetson Nano's wifi drivers aren't updated. In fact, they don't even allow connection, so we must change the driver's preferences.
It is possible, but not with our current knowledge. So we had to find another way.
The network manager of Ubuntu has some useful tools, and Maximilien found one of them, `nmtui`, that was able to check all the wifi networks around us, and to connect to one of them.
It was even able to detect the drivers problem and to fix it.

So we were able to connect to a wifi network, and define it as the default one by editing the configuration files, so that the Jetson Nano will connect to it at startup.
Now we can use the jetson nano with internet.

## Firewall

The next problem is the firewall of the network.
For the tests, I connected both my computer and the Jetson Nano to a mobile hotspot from my phone.
This way, since they were both under the same network, they could coomunicate with each other.
But the firewall of the network wouldn't allow an ssh connection between the Jetson nano and a computer outside the network.
It is not possible to disable the firewall on a phone, for security reasons, so we'll have to connect the jetson nano to a *real* wifi network, created by a confugurable internet box.
For now, I'll stay on this network, but I'll have to change it later.

## SSH server

The ssh server is already configured on the Jetson, with normal settings. But I will customize them a bit to allow X server forwarding, so that we can use graphical interface on the Jetson Nano. It very simple, just change a line in a configuration file and restart the ssh server.
Now I can use graphical interface on the Jetson Nano, even if I'm not connected to it by a wire.

Great achievement: I can now open Visual Studio Code on my computer and connect to the Jetson Nano via SSH using the Remote-SSH tools.
So I can have one VScode running on my computer, connected to the jetson nano by the wired connection, another running simillarily but on the wireless connection, a third running on the jetson nano, reflected by the wired X connection, and a fourth running on the jetson nano, reflected by the wireless X connection, all editing the same files in real time...
However, there is always a slight delay when using the X server connection online, and it is very annoying.
