import lora
import struct
import time
import machine
#from machine import ADC

lora.connect_lora()
from lora import s

#adc = machine.ADC()
#apin = adc.channel(pin='P23')

counter = 0


while True:
    #val = apin()
    #print(val)
    counter += 1
    if counter == 0xFF:
        counter = 0
        pass
        
    s.send(bytes([counter]))
    #s.send(bytes([0x01,0x02]))
    time.sleep(5)
