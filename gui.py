import tkinter as tk
from PIL  import ImageTk, Image
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import sys
from Create_dataset import function

def Train():
    function(usn.get())
    os.system("Train_dataset.py")


def Attendance():
    os.system("Recognise.py")


def AttendanceFolder():
    file = filedialog.askopenfilename(initialdir = r"Attendance", title = "Files")
    os.system(file)

AttendanceSystem = tk.Tk()
AttendanceSystem.title('Attendance System')
AttendanceSystem.geometry('550x400')

tab = ttk.Notebook(AttendanceSystem)

frame1 = ttk.Frame(tab)

tk.Label(frame1, text="Enter Your USN number:", pady=20).grid()

usn = tk.Entry(frame1, width=20, border=2, bg='white')
button1 = tk.Button(frame1, text='Enrol',width=20, command=Train).grid(row=1, column=11, padx=10)
usn.grid(row=1, column=10)



frame2 = ttk.Frame(tab)
button1 = tk.Button(frame2, text="Take Attendance", width=20, pady=10, command=Attendance).pack()
button2 = tk.Button(frame2, text="Attendance Directory", width=20, pady=10, command=AttendanceFolder).pack()

tab.add(frame1, text = "Enrollment")
tab.add(frame2, text = "Attendance")




tab.pack(fill="both", expand=1)



button3 = tk.Button(AttendanceSystem, text="Exit", width=20, command=AttendanceSystem.destroy).pack()




AttendanceSystem.mainloop()
