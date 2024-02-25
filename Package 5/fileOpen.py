# Simple python program with GUI that can open and read contents of the file.
# author: danielCodingGuy

from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfile(initialdir="C:\\Users\\Daniel\\PythonProjects",
                                      title = "File opener",
                                      filetypes = ("text files","*.txt"))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text = "Open", command = "openFile") # Button that uses openFile function.
button.pack()
window.mainloop()