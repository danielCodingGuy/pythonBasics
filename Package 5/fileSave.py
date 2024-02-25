# A simple python program that will save a users text in a file.
# author: danielCodingGuy

from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file",".HTML"),
                                        ("All files",".*")
                                    ])
    if file is None: # This line helps with not getting exceptions in our IDE if file was not saved.
        return
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text = 'Save', command = saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
