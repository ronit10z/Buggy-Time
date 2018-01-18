import tkinter as tk
from tkinter import ttk
import time
import tkinter.filedialog as tkFileDialog
import csv
from collections import defaultdict

import coordinator as coord


def openFile():

  fileName =  tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",
    filetypes = (("csv files","*.csv"),("all files","*.*")))
  return fileName

if __name__ == '__main__':
    root = tk.Tk()
    getFld = tk.IntVar()
    root.wm_title("Poop")
    root.iconbitmap("poop.ico")

    canPing = True
    nameTimesDict = defaultdict(list)

#                                   MENU
#******************************************************************************
    def hello():
        print ("hello!")
    menubar = tk.Menu(root)

    # create a pulldown menu, and add it to the menu bar
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=openFile)
    filemenu.add_command(label="Save", command=hello)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    # create more pulldown menus
    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cut", command=hello)
    editmenu.add_command(label="Copy", command=hello)
    editmenu.add_command(label="Paste", command=hello)
    menubar.add_cascade(label="Edit", menu=editmenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=hello)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    root.config(menu=menubar)

#                                   TABLE
#******************************************************************************
    tableLf = tk.LabelFrame(root, text=" Pusher Times ")
    tableLf.grid(row=0, column=9, columnspan=2, rowspan=8, \
                sticky='NS', padx=5, pady=5)
    tableCanvas = tk.Canvas(tableLf)
    tableCanvas.grid(row=0)

    tableFrame = tk.Frame(tableCanvas)
    tableFrame.grid(row=0, column=0, sticky='nw')

    Can1 = tk.Canvas(tableFrame)
    Can1.grid(row=0, column=0)

    vsbar = ttk.Scrollbar(tableFrame, orient="vertical", command=Can1.yview)
    vsbar.grid(row=0, column=1, sticky='ns')
    Can1.configure(yscrollcommand=vsbar.set)

    hsbar = ttk.Scrollbar(tableFrame, orient="horizontal", command=Can1.xview)
    hsbar.grid(row=1, column=0, sticky='ew')
    Can1.configure(xscrollcommand=hsbar.set)

    # Create a frame to contain the buttons
    frame_buttons = tk.Frame(Can1, bd=2, relief=tk.GROOVE)
    Can1.create_window((0,0), window=frame_buttons,anchor='nw')

    # Bind the buttons frame to a function that fixes the Canvas size
    def resize(event):
        Can1.configure(scrollregion=Can1.bbox("all"), width=235, height=300)
    frame_buttons.bind("<Configure>", resize)

    # Add the buttons to the frame
    rows = 50
    columns = 10

    nameTimesDict["Kevin"].append(13.2)
    nameTimesDict["James"].append(14.1)
    dictKeys = sorted(nameTimesDict.keys())
    entryGrid = [[0]*columns for row in range(rows)]

    for i in range(0,rows):
      if (i < len(dictKeys)):
        currentName = dictKeys[i]
        currentTimes = nameTimesDict[currentName]
      else:
        currentName = None
        currentTimes = None

      for j in range(0,columns):
          entry = ttk.Entry(frame_buttons, text="", width=8)
          entryGrid[i][j] = entry
          if (j == 0 and currentName != None):
              entry.configure(width=15)
              entry.delete(0,tk.END)
              entry.insert(0, currentName)
          elif (currentTimes != None and j < len(currentTimes) + 1):
              entry.configure(width=8)
              entry.delete(0,tk.END)
              entry.insert(0, currentTimes[j - 1])
          entry.grid(row=i, column=j, sticky='news')


#                            FILE MANAGEMENT
#******************************************************************************

    fileLF = ttk.LabelFrame(root, text=" CSV File ")
    fileLF.grid(row=2, columnspan=4, sticky='W', \
                   padx=5, pady=5, ipadx=5, ipady=5)

    fileTextBox = ttk.Entry(fileLF)
    fileTextBox.grid(row=0, column=0, sticky='WE', padx=5, pady=5)

    def browseFile():
      fileName = openFile()
      fileTextBox.insert(0, fileName)

    browse = ttk.Button(fileLF, text=" Browse... ", command=browseFile)
    browse.grid(row=0, column=3, columnspan=2, sticky='W', padx=5, pady=2)


    def inportFile():
      fileName = fileTextBox.get()
      if (fileName.endswith(".csv")):
          with open(fileName) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')


    inport = ttk.Button(fileLF, text=" Import ", command= inportFile)
    inport.grid(row=1, column=0, columnspan=2, sticky='EW', padx=5, pady=2)

    def updateCell(name, value):
      nameTimesDict[name].append(value)

      row = dictKeys.index(name)
      col = len(nameTimesDict[name])

      entry = entryGrid[row][col]
      entry.insert(0, value)

    def test():
      updateCell("Kevin", 12.4)

    def go():
        global canPing
        canPing = False
        trialTime = coord.getTrial()
        popup_bonus(trialTime)

    def popup_bonus(trialTime):
      win = tk.Toplevel()
      win.wm_title("Window")
      win.geometry('150x250')

      tableLf = tk.LabelFrame(win, text="Select a pusher")
      tableLf.grid(row=0, column=0, columnspan=2, rowspan=8, \
                  sticky='NS', padx=5, pady=5)
      tableCanvas = tk.Canvas(tableLf)
      tableCanvas.grid(row=0)

      tableFrame = tk.Frame(tableCanvas)
      tableFrame.grid(row=0, column=0, sticky='nw')

      Can1 = tk.Canvas(tableFrame)
      Can1.grid(row=0, column=0)

      vsbar = ttk.Scrollbar(tableFrame, orient="vertical", command=Can1.yview)
      vsbar.grid(row=0, column=1, sticky='ns')
      Can1.configure(yscrollcommand=vsbar.set)

      mylist = tk.Listbox(Can1, yscrollcommand = vsbar.set)
      for i in range(len(dictKeys)):
         mylist.insert(tk.END, dictKeys[i])

      mylist.pack(side = tk.LEFT, fill = tk.BOTH)
      vsbar.config(command = mylist.yview)

      def grab_name():
        global canPing
        nameidx = mylist.curselection()[0]
        name = mylist.get(nameidx)
        updateCell(name, trialTime)
        canPing = True
        win.destroy()

      b = ttk.Button(win, text="Okay", command=grab_name)
      b.grid(row=12, column=1)


#                              TIMER CONTROL
#******************************************************************************
    def color_change():
        goButton.configure(bg = "gray85")

    goButton = tk.Button(root, text="GO", font=("Helvetica", 16), bg = "lawn green", command = go)
    goButton.grid(row=6, columnspan=4, sticky='NSEW', \
                 padx=5, pady=5, ipadx=5, ipady=5)

    timerLF = tk.LabelFrame(root, text=" Time: ")
    timerLF.grid(row=5, column=1, columnspan=2, sticky='EW', \
                 padx=5, pady=5, ipadx=5, ipady=5)

    timer = tk.Label(timerLF, text= "00:00",font=("Helvetica", 16))
    timer.grid(sticky='EW', padx=5, pady=2)

    export = ttk.Button(fileLF, text=" Export ", command=popup_bonus)
    export.grid(row=2, column=0, columnspan=2, sticky='EW', padx=5, pady=2)

    class Pinger:
        def __init__(self, master):
            self.master = master
            self.ping() # start polling

        def ping(self):
            global canPing
            self.t = time.time()
            # Do something every second if allowed
            if (canPing):
                if (not coord.pingBoth()):
                    goButton.configure(bg = "red")
                else:
                    goButton.configure(bg = "green")

            self.master.after(1000, self.ping)

    pingTimer = Pinger(root)

    root.mainloop()
