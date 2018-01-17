import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    getFld = tk.IntVar()
    root.wm_title("Poop")
    root.iconbitmap("poop.ico")

#                                   MENU
#******************************************************************************
    def hello():
        print ("hello!")
    menubar = tk.Menu(root)

    # create a pulldown menu, and add it to the menu bar
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=hello)
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

    vsbar = tk.Scrollbar(tableFrame, orient="vertical", command=Can1.yview)
    vsbar.grid(row=0, column=1, sticky='ns')
    Can1.configure(yscrollcommand=vsbar.set)

    hsbar = tk.Scrollbar(tableFrame, orient="horizontal", command=Can1.xview)
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
    columns = 50
    names = ["Alice","Bob","Charlie","David","Eve","Frank","Grace","Heidi","Isabella","Judy","Kevin","Lucy","Mallory","Nicole","Oscar","Pat","Richard","Sybil","Trent","Victor","Wendy"]
    for i in range(0,rows):
        for j in range(0,columns):
            entry = tk.Entry(frame_buttons, text="", width=8)
            if (j == 0 and i < len(names)):
                entry.configure(width=15)
                entry.delete(0,tk.END)      
                entry.insert(0, names[i])
            entry.grid(row=i, column=j, sticky='news')

#                              TIMER CONTROL
#******************************************************************************
    def color_change():
        goButton.configure(bg = "gray85")

    goButton = tk.Button(root, text="GO", font=("Helvetica", 16), bg = "lawn green", command = color_change)
    goButton.grid(row=6, columnspan=4, sticky='NSEW', \
                 padx=5, pady=5, ipadx=5, ipady=5)
    
    timerLF = tk.LabelFrame(root, text=" Time: ")
    timerLF.grid(row=5, column=1, columnspan=2, sticky='EW', \
                 padx=5, pady=5, ipadx=5, ipady=5)
    
    timer = tk.Label(timerLF, text= "00:00",font=("Helvetica", 16))
    timer.grid(sticky='EW', padx=5, pady=2)



#                            FILE MANAGEMENT
#******************************************************************************

    fileLF = tk.LabelFrame(root, text=" CSV File ")
    fileLF.grid(row=2, columnspan=4, sticky='W', \
                   padx=5, pady=5, ipadx=5, ipady=5)


    browse = tk.Button(fileLF, text=" Browse... ")
    browse.grid(row=0, column=3, columnspan=2, sticky='W', padx=5, pady=2)

    fileTextBox = tk.Entry(fileLF)
    fileTextBox.grid(row=0, column=0, sticky='WE', padx=5, pady=5)

    inport = tk.Button(fileLF, text=" Import ")
    inport.grid(row=1, column=0, columnspan=2, sticky='EW', padx=5, pady=2)

    export = tk.Button(fileLF, text=" Export ")
    export.grid(row=2, column=0, columnspan=2, sticky='EW', padx=5, pady=2)

    root.mainloop()