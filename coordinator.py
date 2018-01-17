from xbee import XBee
from serial import Serial
import time
import csv

PORT = 'COM3'
BAUD = 9600

# def sendReady(xbee, dest):
# 		message = dest + ": ready"
# 		xbee.tx(dest_addr='\x00\x01', data=message)

# def TakeReading():
# 	ser = Serial(PORT, BAUD)
# 	xbee = XBee(ser)
# 		# send ready messagae to start
# 	sendReady(xbee, "start")

# 	# Wait for and get the response
# 	print("waiting\n")
# 	startMessage = xbee.wait_read_frame()["rf_data"]
# 	startTime = time.time() # take time right away to reduce latency
# 	while (startMessage != "start: line crossed"):
# 			startMessage = xbee.wait_read_frame()["rf_data"]
# 			print(startMessage)
# 			startTime = time.time()
# 	print("done waiting\n")
# 	# send ready message to finish
# 	sendReady(xbee, "finish")

# 	# Wait for and get the response
# 	finishMessage = xbee.wait_read_frame()["rf_data"]
# 	finishTime = time.time() # take time right away to reduce latency
# 	while (finishMessage != "finish: line crossed"):
# 			startMessage = xbee.wait_read_frame()["rf_data"]
# 			finishTime = time.time()

# 	ser.close()
# 	return finishTime - startTime
start_ping_message = 'c'


def ping(message):
	ser = Serial(PORT, BAUD)
	xbee = XBee(ser)
	startTime = time.time()
	xbee.tx(dest_addr='\x00\x01', data=message)

	recievedMessage = xbee.wait_read_frame()["rf_data"]
	while (finishMessage != "finish: line crossed"):
		startMessage = xbee.wait_read_frame()["rf_data"]
		finishTime = time.time()





