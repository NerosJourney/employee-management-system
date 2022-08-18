from tkinter import *
from tkinter import ttk
import requests

resp = ''

def reqFromServer():
    global resp
    r = requests.get('http://localhost:5000/dq/employees')
    print(r.text)
    resp = r


root = Tk()
frm = ttk.Frame(root, padding=25)
frm.grid()
ttk.Label(frm, text="Hello World!    ").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Request", command=reqFromServer).grid(column=0, row=1)
ttk.Label(frm, text=resp).grid(column=1,row=1)
root.mainloop()