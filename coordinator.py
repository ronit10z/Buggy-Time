from xbee import XBee
from serial import Serial
from time import sleep
import csv

PORT = 'COM3'
BAUD = 9600

ser = Serial(PORT, BAUD)

xbee = XBee(ser)
trial = 1
while (True):

    # send ready messagae to start
    sendReady(xbee, "start")

    # Wait for and get the response
    startMessage = xbee.wait_read_frame()["rf_data"]
    startTime = time.time() # take time right away to reduce latency
    while (startMessage != "start: line crossed"):
        startMessage = xbee.wait_read_frame()["rf_data"]
        startTime = time.time

    # send ready message to finish
    sendReady(xbee, "finish")

    # Wait for and get the response
    finishMessage = xbee.wait_read_frame()["rf_data"]
    finishTime = time.time() # take time right away to reduce latency
    while (finishMessage != "finish: line crossed"):
        startMessage = xbee.wait_read_frame()["rf_data"]
        finishTime = time.time


    data = ["Trial %d" % trial, (finishTime-startTime)]
    out = csv.writer(open("myfile.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
    out.writerow(data)
    trial += 1
    input("Press enter for next run")

ser.close()

def sendReady(xbee, dest):
    message = dest + ": ready"
    xbee.tx(dest_addr='\x00\x01', data=message)
