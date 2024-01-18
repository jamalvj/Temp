from tkinter import *
from tkinter import ttk

def einganbe():
    try:
        eingabe_wert = int(tmpentry.get())
        if eingabe_wert <= 28:
            return "green"
        elif 29 <= eingabe_wert <= 31:
            return "yellow"
        elif eingabe_wert >= 32:
            return "red"
    except ValueError:
        return "white" 

def update_color():
    color = einganbe()
    tmplabel.configure(bg=color)
    frmMain.configure(bg=color)
    tmpberechnen.configure(bg=color)



frmMain = Tk()
frmMain.title("Temperatursensors")
frmMain.geometry("400x200")
frmMain.resizable(width=False, height=False)
frmMain.configure()

for row in range(5):
    frmMain.rowconfigure(row, weight=1)

for column in range(4):
    frmMain.columnconfigure(column, weight=1)

tmplabel = Label(master=frmMain, text="aktuelle Temperatur")
tmplabel.grid(row=0, column=0, columnspan=2)

tmpentry = Entry(master=frmMain)
tmpentry.grid(row=0, column=2)

tmpberechnen = Button(master=frmMain, text="Farbe", command=update_color, width=16)
tmpberechnen.grid(row=4, column=2, columnspan=1)

frmMain.mainloop()