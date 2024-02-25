# Simple program that uses GUI in python.
# author: danielCodingGuy

from tkinter import *

window = Tk()
window.geometry("420x420") # This will change the size of our window.
window.title("danielCodingGuy GUI")

icon = PhotoImage(file = 'bateman.jpg') # This will change our icon into PhotoImage.
window.iconphoto(True,icon) # This will display our icon in the corner of the window.
window.config(background = "black") # This will change the color value, you can also use hex values.

window.mainloop() # This function will create an empty window.
