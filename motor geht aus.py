from machine import Pin
from time import sleep

groveled = Pin(18, Pin.OUT)
ml1 = Pin(13, Pin.OUT)
ml2 = Pin(12, Pin.OUT)
mr1 = Pin(11, Pin.OUT)
mr2 = Pin(10, Pin.OUT)


groveled.low()
ml1.low()
ml2.low()
mr1.low()
mr2.low()