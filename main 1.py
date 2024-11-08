from machine import Pin, PWM, ADC
from time import sleep

# Pin-Definitionen
groveled = Pin(27, Pin.OUT)
ledpin = Pin(25, Pin.OUT)   
ml1 = Pin(13, Pin.OUT)
ml2 = Pin(12, Pin.OUT)
mr1 = Pin(11, Pin.OUT)
mr2 = Pin(10, Pin.OUT)

wert_a = ADC(Pin(26))  # ADC-Pin wird definiert A0
wert_d = Pin(8, Pin.IN)  # Digital-Pin wird definiert IC20 
OnBoard = Pin(16, Pin.IN, Pin.PULL_DOWN)  # Onboard-Taster

motor_r = PWM(mr2)
motor_l = PWM(ml2)
motor_r.freq(2000)
motor_l.freq(2000)

def lesen(Art):  # Lesen von Sensorwerten
    if Art == "a":
        return wert_a.read_u16()  # Analogwert zurückgeben
    elif Art == "d":
        return wert_d.value()  # Digitalwert zurückgeben

def fahren(gas_l, gas_r, dauer):
    # Motoren ansteuern
    motor_l.duty_u16(gas_l)
    motor_r.duty_u16(gas_r)
    sleep(dauer)

# Hauptprogrammschleife
while True:
    a_sensor = lesen("a")  # Analogwert lesen
    sleep(0.1)
    groveled.value()=1
    print("Sensorwert ist", sensor)
    
    # Bedingungen für die Motorsteuerung
    if a_sensor < 10000:
        fahren(0, 25000, 0.25)  # Motor nach rechts
        print("Sensor ist im unteren Bereich\n")
        print("Auto fährt rechts\n")
        break
    elif 10000 < a_sensor < 30000:
        # Hier kannst du eine Funktion für den mittleren Bereich hinzufügen
        fahren(20000,20000,0.5)
        print("Sensor im mittleren Bereich.\n")
        print("Auto fährt geradeaus\n ")
        motor_l.duty_u16(0)  # Stoppe den linken Motor
        motor_r.duty_u16(0)
        break# Stoppe den rechten Motor
    elif a_sensor >= 30000:
        print("Sensor im oberen Bereich\n")
        print("Auto fährt links\n")
        fahren(25000, 0, 0.25)
        break# Motor nach links
    if rp2.bootsel_button() ==1:
        fahren(0,0,0)
        print("Programm beendet durch Knopfdruck")
        break
    # Überprüfen, ob der Onboard-Taster gedrückt wird
  
     fahren(0,0,0)   

    sleep(2)