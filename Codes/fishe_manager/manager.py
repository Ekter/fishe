"""program to manage the fishe"""

import time

import rudder
import propeller
import arduino_communicator
import probe_manager


def main():
    print("-----------------------------------------------------LAUNCHING THE CONNECTIONS-----------------------------------------------------")
    try:
        com = arduino_communicator.ArduinoCommunicator()
        time.sleep(5)
        rud = rudder.Rudder(com)
        prop = propeller.Propeller(com)
        probe = probe_manager.ProbeManager(com)
    except Exception as e:
        print("-----------------------------------------------------ERROR-----------------------------------------------------")
        print(e)
        print("-----------------------------------------------------ERROR-----------------------------------------------------")
        return
    print("-----------------------------------------------------CONNECTIONS CORRECT-----------------------------------------------------")

    try:
        rud.start()
        prop.start()
        probe.start()
        time.sleep(5)
        print(com.read())
        # input("-----------------------------press enter to start the fishe demo-----------------------------")
        rud.set_angle(90)
        prop.set_speed(10)
        time.sleep(5)
        prop.set_speed(0)
        time.sleep(1)
        prop.set_speed(-10)
        time.sleep(5)
        prop.set_speed(0)
        time.sleep(1)
        rud.set_angle(60)
        time.sleep(5)
        rud.set_angle(120)
        time.sleep(5)
        rud.set_angle(90)
        time.sleep(1)
        probe.go_down()
        time.sleep(5)
        probe.go_up()
        time.sleep(5)
        probe.stop()
        print("-----------------------------------------------------fishe demo routine ended-----------------------------------------------------")

    except KeyboardInterrupt:
        rud.stop()
        prop.stop()


if __name__ == "__main__":
    main()
