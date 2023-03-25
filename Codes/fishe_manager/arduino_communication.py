import serial
import time

arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

trame = [190, 123, 4, 12, 37]

i=-10
previous_time = 0
while True:
    try:
        # arduino.write(b"a")
        data = arduino.readline()
        if data:
            print(f"->{data}<-")
            # print('Hi Arduino')
            # arduino.write()
        if time.time()>previous_time+1:
            previous_time = time.time()
            # arduino.write(bytes([37]))
            # print(bytes([37]))
            # print(bytes(37))
            i+=1
            if i in range(len(trame)):
                arduino.write(bytes([trame[i]]))
                print(f"sent : {bytes([trame[i]])}'")
    except:
        arduino.close()

