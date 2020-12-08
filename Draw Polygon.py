numSides = int(input("The turtle will draw a n-sided polygon. Please input n: "))


#Let's make the turtle draw a polygon
#First import the module turtle
import turtle

#Second open a window
wn = turtle.Screen()

#Third create a turtle and assign it to a variable
myTurtle = turtle.Turtle()



angleToTurn = 360/numSides
sideLength = 200*3.14159265/numSides

#Draw the polygon
def drawPolygon():
    for yee in range(1, numSides+1):
        myTurtle.forward(sideLength)
        myTurtle.left(angleToTurn)

#Wait for the user to close the window
drawPolygon()
wn.mainloop()
