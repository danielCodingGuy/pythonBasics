from tkinter import *
from ball import *
import time

window = Tk()

Width = 500
Height = 500

canvas = Canvas(window,width = Width,height = Height)
canvas.pack()

volley_ball = Ball(canvas,0,0,80,1,1,"yellow")
tennis_ball = Ball(canvas,0,0,30,4,3,"white")
soccer_ball = Ball(canvas,0,0,90,8,7,"black")
basket_ball = Ball(canvas,0,0,100,5,2,"orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    soccer_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()