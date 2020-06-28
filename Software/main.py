import lora
import struct
import time
import machine
from machine import ADC

#The sensor used in this project is MCP9700T-E
#It is an cheap temperature sesnor with built in compensation and linearization
#You can compensate for self heating of teh sensor but it is not used in this code.
# Accurecy is +-2 degrees C
#Volatge offset at 0 degrees C is 500mV
#Temperature coefficient is 10mV/degree C

#Function to calculate temperature: Vout = Tc * Ta * V0
#Vout   = Volate output from sensor
#Tc     = Temperature Coefficient
#Ta     = Ambient temperature
#T0     = Sensor output voltage at 0°C

#Values for the temperature calculations
T0 = 500
Tc = 10
Temperature = 0

#Create a LoRa socket
lora.connect_lora()
from lora import s

#Initiate the ADC for pin 16
adc = machine.ADC()
apin = adc.channel(pin='P16')


while True:
    #Take a analog measurement
    #val = apin()

    #Test Value
    val = 900

    #Calculations for the temperature sensor
    Temperature = (val*3300)/4096
    Temperature -= T0
    Temperature /= Tc

    #Multiply teh value by 10 to get a decimal accuracy of 0.1
    Temperature *= 10           # remember to devide by 10 on reciveing end

    #Split the temperature measurement into two bytes (Upper and Lower)
    Lower = int(Temperature) & 0xff
    Upper = int(Temperature) >> 8

    #Send the two bytes to the TTN server
    s.send(bytes([Upper, Lower]))
    #print(Temperature/10)
    time.sleep(5)
