from xbee import XBee
from serial import Serial
from time import sleep

PORT = 'COM3'
BAUD = 9600

ser = Serial(PORT, BAUD)

xbee = XBee(ser)
while (True):
    # Send the string 'Hello World' to the module with MY set to 1
    xbee.tx(dest_addr='\x00\x01', data=input("type message: "))

    # Wait for and get the response
    new_data = xbee.wait_read_frame()
    print(new_data["rf_data"])
    sleep(.5)

ser.close()
