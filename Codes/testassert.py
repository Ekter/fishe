
def send_data():
    status = None
    data=[]
    try:
        with open('data_to_send.csv', 'r') as f:
            data = f.readlines()
    except Exception as e:
        print(e)
        status = e
    # print(data[0]=="MeasureId,Temperature,PH,Turbidity,Zposition,XPosition,YPosition")
    try:
        assert data[0].strip()=="MeasureId,Temperature,PH,Turbidity,Zposition,XPosition,YPosition", "data_to_send.csv format error"
        
    data = data[1:]

    print("ok")



send_data()
