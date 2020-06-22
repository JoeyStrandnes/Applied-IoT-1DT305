import lora
import struct
import time

lora.connect_lora()
from lora import s


while True:
    #s.send(byte(0x69))
    s.send(bytes([0x01,0x02]))
    time.sleep(5)
