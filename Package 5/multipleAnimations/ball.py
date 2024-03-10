#Class that will create ball that multipleAnimations.py gonna move around.
#author: danielCodingGuy

class Ball:

    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color): #This contains the coords of our object and some of its properties.
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill = color)
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        
        if (coordinates[2]>=(self.canvas.winfo_width()) or coordinates[0]<0): #Theese ifs make our ball bounce when coming in contact with borders of our window.
            self.xVelocity = -self.xVelocity
        if (coordinates[3]>=(self.canvas.winfo_height()) or coordinates[1]<0):
            self.yVelocity = -self.yVelocity

        self.canvas.move(self.image,self.xVelocity,self.yVelocity)
