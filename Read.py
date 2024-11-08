from machine import Pin,Timer,ADC
from time import sleep

def readSensor():
    Sensor= ADC(Pin(27,Pin.IN))
    
    return Sensor.read_u16()

while True:
    
    print(readSensor())
    sleep(0.5)
