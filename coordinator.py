from xbee import XBee
from serial import Serial
import time
import csv

PORT = 'COM3'
BAUD = 9600

start_ready_message = 'a'
start_line_crossed_message = 'b'
start_ping_message = 'c'
finish_ready_message = 'd'
finish_line_crossed_message = 'e'
finish_ping_message = 'f'

def ping(message):
    timeOut = 0.2
    ser = Serial(PORT, BAUD)
    xbee = XBee(ser)
    startTime = time.time()
    xbee.tx(dest_addr='\x00\x01', data=message)
    while not ser.inWaiting():
        finishTime = time.time()
        if (finishTime-startTime > timeOut):
            return False
    recievedMessage = xbee.wait_read_frame()["rf_data"].decode('utf8')
    if (recievedMessage != message):
        return False

    ser.close()
    return True

def pingStart():
    return ping(start_ping_message)

def pingFinish():
    return ping(finish_ping_message)

def pingBoth():
    return pingStart() and pingFinish()

def getTrial():
    timeOut = 60
    counterLimit = 50
    ser = Serial(PORT, BAUD, timeout=1)
    xbee = XBee(ser)

    # Send Ready messages
    xbee.tx(dest_addr='\x00\x01', data=start_ready_message)
    xbee.tx(dest_addr='\x00\x01', data=finish_ready_message)

    # Wait for start line crossed
    beginTime = time.time()
    while not ser.inWaiting(): #check for no response and end if no response
        endTime = time.time()
        if (endTime-beginTime > timeOut):
            return None
    startMessage = xbee.wait_read_frame()["rf_data"].decode('utf8')
    startTime = time.time()
    counter = 0
    while(startMessage != start_line_crossed_message):
        if (counter > counterLimit): #Try for the correct message counterLimit times
            return None
        beginTime = time.time()
        while not ser.inWaiting(): #check for no response and end if no response
            endTime = time.time()
            if (endTime-beginTime > timeOut):
                return None
        startMessage = xbee.wait_read_frame()["rf_data"].decode('utf8')
        startTime = time.time()
        counter += 1

    # Wait for finish line crossed
    beginTime = time.time()
    while not ser.inWaiting(): #check for no response and end if no response
        endTime = time.time()
        if (endTime-beginTime > timeOut):
            return None
    finishMessage = xbee.wait_read_frame()["rf_data"].decode('utf8')
    finishTime = time.time()

    counter = 0
    while(finishMessage != finish_line_crossed_message):
        if (counter > counterLimit): #Try for the correct message counterLimit times
            return None
        beginTime = time.time()
        while not ser.inWaiting(): #check for no response and end if no response
            endTime = time.time()
            if (endTime-beginTime > timeOut):
                return None
        finishMessage = xbee.wait_read_frame()["rf_data"].decode('utf8')
        finishTime = time.time()
        counter += 1

    trialTime = finishTime - startTime

    return trialTime
