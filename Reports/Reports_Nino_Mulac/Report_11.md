pip problems

ports problems

# Eleventh report -- 01/2/2023

This week I tried to solve my Jetson Nano server problems. It will run as an web server, being a wifi hotspot.

I had some installation problems, because the jetson nano uses python 2.7 as the default python version, and python 3.6 minimum is required to run a server with Django. Plus, the default python package manager, to install additional modules, isn't installed by default, and if you install it, it will of course be installed for the default python, aka 2.7. Django also needs a virtual environnement for security reasons, since running a web server directly on a computer is quite dangerous. So I had to install `python3-pip`, `python3-venv`, and run `pip upgrade --force` to change the default version to 3.6. But with all this done, I can run the server using a simple bash script, see [runserver.sh](/Codes/fishe_server/runserver.sh), installing all the requirements anytime I launch. I can also modify the code, the server will be modified directly, since Django supports hot reloading. So I can run the server quite easily now.

But, I can't even see the server outside the board, because of ports problems, even on the same network.
I can check it actually runs using Vscode's ports redirection, but I don't know how it works, and probably can't apply it to the raspberry pi.

The fact that I can't see it is really strange since I removed all firewalls from the Jetson Nano, but I still see it as closed, and I don't understand how VScode actually does to redirect a port my computer can't see. Maybe it uses the ssh connection to create an http bridge? Anyway, I need to make more tests, maybe be trying to make the Nano a wifi hotspot, to ensure it isn't a wifi problem. For example, the Unice Hotspot blocks everything, so I can only use my phone's hotspot for tests.