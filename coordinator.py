from xbee import XBee
from serial import Serial
import time
import csv

PORT = 'COM3'
BAUD = 9600

trial = 1

def sendReady(xbee, dest):
		message = dest + ": ready"
		xbee.tx(dest_addr='\x00\x01', data=message)

def TakeReading():
	global trial
	ser = Serial(PORT, BAUD)
	xbee = XBee(ser)
		# send ready messagae to start
	sendReady(xbee, "start")

	# Wait for and get the response
	print("waiting\n")
	startMessage = xbee.wait_read_frame()["rf_data"]
	startTime = time.time() # take time right away to reduce latency
	while (startMessage != "start: line crossed"):
			startMessage = xbee.wait_read_frame()["rf_data"]
			print(startMessage)
			startTime = time.time()
	print("done waiting\n")
	# send ready message to finish
	sendReady(xbee, "finish")

	# Wait for and get the response
	finishMessage = xbee.wait_read_frame()["rf_data"]
	finishTime = time.time() # take time right away to reduce latency
	while (finishMessage != "finish: line crossed"):
			startMessage = xbee.wait_read_frame()["rf_data"]
			finishTime = time.time()

	ser.close()
	return finishTime - startTime
			# data = ["Trial %d" % trial, (finishTime - startTime)]
			# out = csv.writer(open("myfile.csv","a"), delimiter=',',quoting=csv.QUOTE_ALL)
			# out.writerow(data)
			# trial += 1