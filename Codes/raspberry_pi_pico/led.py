import machine
import socket
import math
import utime
import network
import time
import urequests
import random
import ujson

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("here", "Plik est grand et divin")

# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
print('connected')
ip = wlan.ifconfig()[0]
print('IP: ', ip)


# Get current time
r = urequests.get('http://worldtimeapi.org/api/ip')
result = str(r.content)
print(result)
startTime = result[int(result.find("datetime")) + 11:30 + result.find("datetime")]
print(startTime)

r2 = urequests.get("http://192.168.34.199/api/measure/?format=api")
print(str(r2.__dict__))
print(r2.content.decode())
for i in range(10):
    r3 = urequests.post("http://192.168.34.199/api/measure/", headers = {'content-type': 'application/json'}, data = ujson.dump("data",{
    "temperature": random.randint(0,20),
    "pH": random.randint(0,1400)/100,
    "turbidity": random.randint(0,10000),
    "x_position": random.randint(-500,500)/100,
    "y_position": random.randint(-500,500)/100,
    "z_position": random.randint(-500,500)/1000-i,
    "probe": 1}))
    if r3.status_code == 200:
        print("tvgjhrfbkdcxslw")

