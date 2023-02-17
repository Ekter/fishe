#!/bin/bash


source venv/bin/activate;
pip3 install -r requirements.txt;
sudo python3 manage.py runserver 0.0.0.0:80;