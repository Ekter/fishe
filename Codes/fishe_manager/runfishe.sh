#!/bin/bash


source fishe_server/venv/bin/activate;
pip3 install -r requirements.txt;
sudo fishe_server/venv/bin/python3 fishe_server/manage.py runserver 0.0.0.0:80 & 
sudo fishe_server/venv/bin/python3 manager.py && fg
