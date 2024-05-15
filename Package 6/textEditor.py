#Simple text editor w/ some customization options made using python.
#author: danielCodingGuy

import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

#Function which allows user to change to font color depending on users preference.
def change_color():
    color = colorchooser.askcolor(title="pick a color.")
    text_area.config(fg = color) 

#Function that allows user to change font family and size.
def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))

#Function which allows user to create new text file.
def new_file():
    window.title("New Text File")
    text_area.delete(1.0, END)

#Function which allows user to open existing text files.
def open_file():
    file = askopenfilename(defaultextension=".txt", file=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, "r")

        text_area.insert(1.0, file.read())

    except Exception:
        print("Couldn't read file.")

    finally:
        file.close()

#Function that allows user to save the currently opened file.
def save_file():
    file = filedialog.asksaveasfilename(initialfile = "Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    
    if file is None:
        return
    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))
        except Exception:
            print("couldn't save file.")
        finally:
            file.close()

#Function which allows user to cut some text from the file.
def cut():
    text_area.event_generate("<<Cut>>")

#Function which allows to user to copy some of the text.
def copy():
    text_area.event_generate("<<Copy>>")

#Function which allows user to pase some of the text.
def paste():
    text_area.event_generate("<<Paste>>")

#Function which provides some info.
def about():
    showinfo("About program", "This is a simple text editor written in python by danielCodingGuy.")

def quit():
    window.destroy()

#Setting the window and title.
window = Tk()
window.title("Notepad")
file = None

#Window size, getting the users display resolution.
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

#Setting font style.
font_name = StringVar(window)
font_name.set("Arial")

#Setting font size.
font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

#Setting the scroll bar to operate easier in our window.
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

#Setting the button to change the font color.
color_button = Button(frame, text="color", command=change_color)
color_button.grid(row = 0, column = 0)

#Setting the button with slider to set fonts.
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row = 0, column = 1)

#Setting the spinbox with font sizes.
size_box = Spinbox(frame, from_ = 1, to = 100, textvariable=font_size, command=change_font)
size_box.grid(row = 0, column = 2)

#Setting the menu.
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label="File", menu=file_menu)

#Setting up the file menu list with buttons.
file_menu.add_command(label = "New", command=new_file)
file_menu.add_command(label = "Open", command=open_file)
file_menu.add_command(label = "Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command=quit)

#Setting up the edit menu list with buttons.
edit_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Edit", menu=edit_menu)
edit_menu.add_command(label = "Cut", command=cut)
edit_menu.add_command(label = "Copy", command=copy)
edit_menu.add_command(label = "Paste", command=paste)

#Setting up the help menu
help_menu = Menu(menu_bar, tearoff = 0)
help_menu.add_cascade(label = "Help", menu=help_menu)
edit_menu.add_command(label = "About", command=about)

window.mainloop()