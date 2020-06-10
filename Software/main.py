import pycom
import time
from uModBus.serial import Serial


pycom.heartbeat(False)


uart_id = 0x01
modbus_obj = Serial(uart_id, pins=('P9', 'P10'))

#Modbus Slave & Holding Register setup for M3-Flow-Meter (Eletta FLow AB)
#Register from 0x10-0x15 (16-21 dec)
#16-bit signed values
#Devide all data with 100 for correct value
slave_addr=0x01
starting_address=0x10
register_quantity=5
signed=True


while True:

    register_value = modbus_obj.read_holding_registers(slave_addr, starting_address, register_quantity, signed)
    print('Holding register value: ' + ' '.join('{:d}'.format(x) for x in register_value/100))
    time.sleep(1)
