#Simple clock app with GUI made in python.
#author: danielCodingGuy

from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p") #This line of code gonna show us the hour:minute:second and am/pm.
    time_label.config(text=time_string)

    day_string = strftime("%A") #This line of code gonna show us the day.
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y") #This line of code gonna show us the date.
    date_label.config(text=date_string)

    time_label.after(1000,update)

window = Tk()

time_label = Label(window, font=("Calibri",50,), fg="#FFFFFF", bg="black") #Here we can customize the looks of time.
time_label.pack()

day_label = Label(window, font=("Calibri",25,), fg="#FFFFFF", bg="black") #Here we can customize the looks of day.
day_label.pack()

date_label = Label(window, font=("Calibri",30,), fg="#FFFFFF", bg="black") #Here we can customize the looks of date.
date_label.pack()

update()

window.mainloop()
