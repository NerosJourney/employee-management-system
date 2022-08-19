from tkinter import *
from tkinter import ttk
import requests

resp = ''

def reqFromServer():
    global resp
    r = requests.get('http://localhost:5000/dq/employees')
    print(r.text)
    resp = r.text
    update_emps()


root = Tk()
frm = ttk.Frame(root, padding=25)
frm.grid()
ttk.Label(frm, text="Hello World!    ").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Request", command=reqFromServer).grid(column=0, row=1)
emps = ttk.Label(frm, text=resp)
emps.grid(column=1,row=1)

def update_emps():
    global emps
    emps["text"] = resp

root.mainloop()