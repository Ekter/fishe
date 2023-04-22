"""main class of the probe, with attributes for each sensor"""
from thermometer import Thermometer
from pHMeter import PHMeter
from turbiditySensor import TurbiditySensor
import secret_data
import uos
import network
import time
import urequests
import random
import ujson


class Probe:
    "probe class"

    def __init__(self, pH_meter : PHMeter, thermometer : Thermometer, turbo_sensor : TurbiditySensor,probe_id : int = 0):
        self.pHMeter = pH_meter
        self.thermometer = thermometer
        self.turboSensor = turbo_sensor
        listdir = uos.listdir()
        self.measureId = 0
        self.data_file = "data_to_send.csv"
        self.probeId = probe_id
        if self.data_file not in listdir:
            self.generate_data_file()
        self.connect_wifi()


    def connect_wifi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(secret_data.wifi_id, secret_data.pswd)

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


    def generate_data_file(self):
        with open("data_to_send.csv","w") as f:
            f.write("MeasureId,ProbeID,Temperature,PH,Turbidity,Zposition,XPosition,YPosition,Date\n")


    def measure(self):
        ph = self.pHMeter.measure()
        temperature = self.thermometer.measure()
        turbidity = self.turboSensor.measure()
        with open(self.data_file,"a") as data:
            data.write("{self.measureId},{self.probeId},{temperature},{ph},{turbidity},{0},{0},{0}")
        print(f"""pH : {ph}
Temperature : {temperature}
Turbidity : {turbidity}
""")


    def test(self):
        self.pHMeter.test()
        self.thermometer.test()
        self.turboSensor.test()


    def send_data(self):
        self.connect_wifi()
        with open(self.data_file) as data_raw:
            data = data_raw.readlines()
            if data[0].strip()!="MeasureId,ProbeID,Temperature,PH,Turbidity,Zposition,XPosition,YPosition,Date":
                self.generate_data_file()

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
