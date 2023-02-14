import machine, onewire, ds18x20, time
 
ds_pin = machine.Pin(26)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
value = []
roms = ds_sensor.scan()
 
print('Found DS18B20 : ', roms)
 
while True:
    
  ds_sensor.convert_temp()
  for i in range(0,10):
    for rom in roms:
      value.append(ds_sensor.read_temp(rom))
    time.sleep(0.05)
  value.sort()
  average = sum(value[2:8])/6
  
  print("Temp")
  print(average)
  
  time.sleep(0.5)
  value = []