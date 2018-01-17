from Tkinter import *
import tkinter as tk
import Tkconstants, tkFileDialog
import tkMessageBox
from coordinator import *
import csv


names = ["Kevin"]
root = Tk()
root.minsize(width=500, height=500)
root.columnconfigure(0, weight=1)

canvas = None
frame = None
 
def donothing():
	 x = 0
 
def openFile():
	global names
	fileName =  tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",
		filetypes = (("csv files","*.csv"),("all files","*.*")))
	with open(fileName) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		names = [row[0] for row in readCSV]
	drawSpreadSheet()

def drawSpreadSheet():
	width = 5
	for i in range(len(names)): #Rows
		for j in range(width): #Columns
			if (j == 0):
				b = Entry(frame, text="")
				b.grid(row=i, column=j)
				b.insert(0, names[i])
			else:
				b = Entry(frame, text="")
				b.grid(row=i, column=j)

def clearSpreadSheet():
	for i in range(len(names)): #Rows
		for j in range(width): #Columns
			if (j == 0):
				b = Entry(frame, text="")
				b.grid(row=i, column=j)
				b.insert(0, names[i])
			else:
				b = Entry(frame, text="")
				b.grid(row=i, column=j)



def on_configure(event):
	# update scrollregion after starting 'mainloop'
	# when all widgets are in canvas
	canvas.configure(scrollregion=canvas.bbox('all'))

def helloCallBack():
   tkMessageBox.showinfo( "Arduino Time", "Ping Time" + str(TakeReading()))
		 
def main():
	global canvas
	global frame
	print("loop")

	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="New", command=donothing)
	filemenu.add_command(label="Open", command=openFile)
	filemenu.add_command(label="Save", command=donothing)
	filemenu.add_command(label="Clear", command=clearSpreadSheet)

	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=root.quit)
	menubar.add_cascade(label="File", menu=filemenu)
	 
	helpmenu = Menu(menubar, tearoff=0)
	helpmenu.add_command(label="Help Index", command=donothing)
	helpmenu.add_command(label="About...", command=donothing)
	menubar.add_cascade(label="Help", menu=helpmenu)
	

	root.config(menu=menubar)
	canvas = tk.Canvas(root)

	

	# update scrollregion after starting 'mainloop'
	# when all widgets are in canvas
	canvas.bind('<Configure>', on_configure)

	# --- put frame in canvas ---

	frame = Frame(canvas)
	canvas.create_window((0,0), window=frame, anchor='nw')

	scrollbar = Scrollbar(root, command=canvas.xview, orient=HORIZONTAL)
	scrollbar.pack(side=BOTTOM, fill='x')
	canvas.configure(xscrollcommand = scrollbar.set)

	scrollbar = Scrollbar(root, command=canvas.yview)
	scrollbar.pack(side=RIGHT, fill='y')
	canvas.configure(yscrollcommand = scrollbar.set)

	canvas.pack(side=tk.LEFT)


	readyButton = Button(root, text ="Ready", command = helloCallBack)
	readyButton.pack()

	benchMark = Button(root, text ="benchMark", command = donothing)
	benchMark.pack()

	drawSpreadSheet()
	
	root.mainloop()


if __name__ == '__main__':
	main()
 
