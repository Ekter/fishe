#!/bin/bash


source venv/bin/activate;
pip3 install -r requirements.txt;
sudo venv/bin/python3 fishe_server/manage.py runserver 0.0.0.0:80 & 
sudo venv/bin/python3 manager.py && fg
