import probe
import pHMeter
import thermometer
import tdsSensor

probe = probe.Probe(pHMeter.PHMeter(), thermometer.Thermometer(), tdsSensor.TDSSensor())
probe.test()
while True:
    probe.measure()
probe.send_data()
