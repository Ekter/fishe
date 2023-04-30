# post data from data_to_send.csv to 198.162.100.1:8080/api/measure

# data_to_send.csv format:
# MeasureId,Temperature,PH,Turbidity,Zposition,XPosition,YPosition
# 1,10,7.02,0.3,-110,100,400


import urequests
import time

TEMPLATE="MeasureId,Temperature,PH,Turbidity,Zposition,XPosition,YPosition"

default_data = {"MeasureId": "1",
                "Temperature": "10",
                "PH": "7.02",
                "Turbidity": "0.3",
                "Zposition": "-110",
                "XPosition": "100",
                "YPosition": "400",
                "ErrorStatus": None}



def post_data(data_to_send:dict[str,str],nb_attempt=10):
    for i in range(nb_attempt):
        try:
            r = requests.post("http://198.162.100.1:8080/api/measure", data=data_to_send)
            if r.status_code == 200:
                return True
        except Exception as e:
            print(e)


def send_data():
    status = None
    data = []
    try:
        with open('data_to_send.csv', 'r') as f:
            data = f.readlines()
    except Exception as e:
        print(e)
        status = e
    try:
        assert data[0]=="MeasureId,Temperature,PH,Turbidity,Zposition,XPosition,YPosition", "data_to_send.csv format error"
        data = data[1:]
        for line in data:
            line = line.split(',')
            assert len(line)==7, "data_to_send.csv format error"
            data_to_send = {
                "MeasureId": line[0],
                "Temperature": line[1],
                "PH": line[2],
                "Turbidity": line[3],
                "Zposition": line[4],
                "XPosition": line[5],
                "YPosition": line[6],
                "ErrorStatus": status
            }
            post_data(data_to_send)
            time.sleep(0.01)
    except AssertionError as e:
        print(e)
        status = e
        repair_data()
    except Exception as e:
        print(e)
        status = e


def repair_data():
    status = None
    try:
        with open('data_to_send.csv', 'w') as f:
            f.write("MeasureId,Temperature,PH,Turbidity,Zposition,XPosition,YPosition\n")
    except Exception as e:
        print(e)
        status = e
    data_=dict(**default_data)
    data_["ErrorStatus"]=status
    post_data(data_to_send=data_)
