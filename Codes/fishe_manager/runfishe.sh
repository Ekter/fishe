#!/bin/bash


source venv/bin/activate;
sudo -H pip3 install -r requirements.txt;
# UUID=$(grep uuid /etc/NetworkManager/system-connections/Hotspot | cut -d= -f2);
# nmcli con up uuid $UUID;
sudo venv/bin/python3 fishe_server/manage.py runserver 0.0.0.0:80 & 
sudo /usr/bin/python3 manager.py && fg
