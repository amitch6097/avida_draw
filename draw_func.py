import turtle

class DrawSymbols():

    def __init__(self, sot):

        self._sot = sot
        self._x = -620
        self._y = 327
        turtle.tracer(300)

    def drawCircleLeft(self, bcolor):

        s = self._sot * 2.5
        turtle.pencolor('black')

        turtle.penup()
        turtle.left(45)
        turtle.forward(self._sot * (1 / (2 ** .5)))
        turtle.right(135)
        turtle.forward(s / 2)
        turtle.left(90)
        turtle.pendown()

        turtle.fillcolor(bcolor) #yellow
        turtle.begin_fill()
        turtle.forward(s / 2)
        turtle.left(90)
        turtle.forward(s)
        turtle.left(90)
        turtle.forward(s)
        turtle.left(90)
        turtle.forward(s)
        turtle.left(90)
        turtle.forward(s / 2)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(s * .03)
        turtle.left(90)
        turtle.forward(s * .1)
        turtle.pendown()

        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.forward(s * .134)
        turtle.right(90)
        turtle.circle(s * .242275, 225)
        turtle.left(90)
        turtle.forward(s * .21)
        turtle.right(135)
        turtle.forward(s * .39)
        turtle.right(90)
        turtle.forward(s * .39)
        turtle.right(135)
        turtle.forward(s * .21)
        turtle.left(90)
        turtle.circle(-s * .376, 225)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(s * .03)
        turtle.left(90)
        turtle.forward(s * .1)
        turtle.backward(s / 2)
        turtle.left(135)
        turtle.backward(self._sot * (1 / (2 ** .5)))
        turtle.right(45)

    def drawCircleRight(self, bcolor):

        s = self._sot * 2.5
        turtle.pencolor('black')

        turtle.penup()
        turtle.left(45)
        turtle.forward(self._sot * (1 / (2 ** .5)))
        turtle.right(135)
        turtle.forward(s / 2)
        turtle.left(90)
        turtle.pendown()

        turtle.fillcolor(bcolor) #magenta
        turtle.begin_fill()
        turtle.forward(s / 2)
        turtle.left(90)
        turtle.forward(s)
        turtle.left(90)
        turtle.forward(s)
        turtle.left(90)
        turtle.forward(s)
        turtle.left(90)
        turtle.forward(s / 2)
        turtle.end_fill()

        turtle.penup()
        turtle.backward(s * .03)
        turtle.left(90)
        turtle.forward(s * .1)
        turtle.pendown()

        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.forward(s * .134)
        turtle.left(90)
        turtle.circle(-s * .242275, 225)
        turtle.right(90)
        turtle.forward(s * .21)
        turtle.left(135)
        turtle.forward(s * .39)
        turtle.left(90)
        turtle.forward(s * .39)
        turtle.left(135)
        turtle.forward(s * .21)
        turtle.right(90)
        turtle.circle(s * .376, 225)
        turtle.end_fill()

        turtle.penup()
        turtle.forward(s * .03)
        turtle.right(90)
        turtle.forward(s * .1)
        turtle.backward(s / 2)
        turtle.left(135)
        turtle.backward(self._sot * (1 / (2 ** .5)))
        turtle.right(45)

    def drawX(self):

        turtle.pencolor('#7e7e7e') #gray
        turtle.left(45)
        turtle.forward(self._sot * (2 / (2 ** .5)))
        turtle.penup()
        turtle.left(135)
        turtle.forward(self._sot)
        turtle.pendown()
        turtle.left(135)
        turtle.forward(self._sot * (2 / (2 ** .5)))
        turtle.left(45)
        turtle.penup()
        turtle.backward(self._sot)
        turtle.pendown()

    def drawRight(self):

        turtle.pencolr('black')
        turtle.penup()
        turtle.forward(self._sot / 2)
        turtle.right(90)
        turtle.forward(self._sot / 2)
        turtle.left(90)

        turtle.pendown()
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.forward(self._sot)
        turtle.left(90)
        turtle.forward(self._sot * 2)
        turtle.left(90)
        turtle.forward(self._sot * 2)
        turtle.left(90)
        turtle.forward(self._sot * 2)
        turtle.left(90)
        turtle.forward(self._sot)
        turtle.end_fill()

        turtle.penup()
        turtle.left(90)
        turtle.forward(self._sot / 2)
        turtle.penup()
        turtle.right(45)

        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.pendown()
        turtle.forward(self._sot / (2 / (2 ** .5)))
        turtle.left(90)
        turtle.forward(self._sot / (2 / (2 ** .5)))
        turtle.left(135)
        turtle.forward(self._sot / 4)
        turtle.right(90)
        turtle.forward(self._sot / 2)
        turtle.left(90)
        turtle.forward(self._sot / 2)
        turtle.left(90)
        turtle.forward(self._sot / 2)
        turtle.right(90)
        turtle.forward(self._sot / 4)
        turtle.end_fill()

        turtle.penup()
        turtle.left(90)
        turtle.backward(self._sot / 2)

    def drawLeft(self):

        turtle.pencolor('black')

        turtle.penup()
        turtle.forward(self._sot / 2)
        turtle.right(90)
        turtle.forward(self._sot / 2)
        turtle.left(90)

        turtle.pendown()
        turtle.fillcolor("red")
        turtle.begin_fill()
        turtle.forward(self._sot)
        turtle.left(90)
        turtle.forward(self._sot * 2)
        turtle.left(90)
        turtle.forward(self._sot * 2)
        turtle.left(90)
        turtle.forward(self._sot * 2)
        turtle.left(90)
        turtle.forward(self._sot)
        turtle.end_fill()

        turtle.penup()
        turtle.left(90)
        turtle.forward(self._sot / 2)
        turtle.penup()
        turtle.left(45)

        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.pendown()
        turtle.forward(self._sot / (2 / (2 ** .5)))
        turtle.right(90)
        turtle.forward(self._sot / (2 / (2 ** .5)))
        turtle.right(135)
        turtle.forward(self._sot / 4)
        turtle.left(90)
        turtle.forward(self._sot / 2)
        turtle.right(90)
        turtle.forward(self._sot / 2)
        turtle.right(90)
        turtle.forward(self._sot / 2)
        turtle.left(90)
        turtle.forward(self._sot / 4)
        turtle.end_fill()

        turtle.penup()
        turtle.left(90)
        turtle.backward(self._sot / 2)

    def drawSpace(self):
        turtle.penup()
        turtle.forward(self._sot * 3)
        turtle.pendown()

    def drawNutrient(self):
        turtle.pencolor('black')
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.forward(self._sot)
        turtle.left(90)
        turtle.forward(self._sot)
        turtle.left(90)
        turtle.forward(self._sot)
        turtle.left(90)
        turtle.forward(self._sot)
        turtle.left(90)
        turtle.end_fill()

    def newLine(self, ytemp):
        turtle.penup()
        turtle.goto(self._x, ytemp)
        turtle.pendown()

    def drawE(self):

        s = self._sot * 2.5
        turtle.pencolor('black')

        turtle.penup()
        turtle.left(45)
        turtle.forward(self._sot * (1 / (2 ** .5)))
        turtle.right(135)
        turtle.forward(s / 2)
        turtle.left(90)
        turtle.pendown()

        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.circle(s / 2)
        turtle.left(90)
        turtle.forward(s / 4)
        turtle.right(90)
        turtle.circle(s / 4)
        turtle.end_fill()

        turtle.penup()
        turtle.left(90)
        turtle.forward(s / 4)
        turtle.right(45)
        turtle.backward(self._sot * (1 / (2 ** .5)))
        turtle.right(45)

    def drawNutrient2(self):
        turtle.pencolor('white')
        turtle.fillcolor("blue")
        turtle.penup()
        turtle.forward(self._sot * .5)
        turtle.right(90)
        turtle.forward(self._sot*.2)
        turtle.left(90)
        turtle.pendown()

        turtle.begin_fill()
        turtle.circle((self._sot*.5) + (self._sot*.2))
        turtle.end_fill()

        turtle.penup()
        turtle.left(90)
        turtle.forward(self._sot * .2)
        turtle.right(90)
        turtle.backward(self._sot * .5)
        turtle.pendown()

    def drawE2(self):
        turtle.pencolor('white')
        turtle.fillcolor("blue")
        turtle.penup()
        turtle.forward(self._sot *.5)
        turtle.right(90)
        turtle.forward(self._sot * .5)
        turtle.left(90)
        turtle.pendown()

        turtle.begin_fill()
        turtle.circle((self._sot * .5) + (self._sot * .5))

        turtle.penup()
        turtle.left(90)
        turtle.forward(self._sot * .5)
        turtle.right(90)
        turtle.pendown()
        turtle.circle(self._sot*.5 + (self._sot * .0))
        turtle.end_fill()

        turtle.penup()
        turtle.left(90)
        turtle.forward(self._sot*.0)
        turtle.right(90)
        turtle.backward(self._sot *.5)
        turtle.pendown()

    def drawStart(self):


        turtle.pencolor('#009900') #green
        turtle.width(3)

        turtle.penup()
        turtle.right(90)
        turtle.forward(self._sot)
        turtle.left(90)

        turtle.pendown()
        turtle.forward(self._sot *.414)
        turtle.left(45)
        turtle.forward(self._sot *.828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .414)
        #turtle.circle(self._sot)
        turtle.penup()

        turtle.left(90)
        turtle.forward(self._sot)
        turtle.right(90)
        turtle.backward(self._sot)

    def drawEnd(self):
        turtle.pencolor('#ff0000')  # red
        turtle.width(7)

        turtle.penup()
        turtle.right(90)
        turtle.forward(self._sot)
        turtle.left(90)

        turtle.pendown()
        turtle.forward(self._sot * .414)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .828)
        turtle.left(45)
        turtle.forward(self._sot * .414)
        # turtle.circle(self._sot)
        turtle.penup()

        turtle.left(90)
        turtle.forward(self._sot)
        turtle.right(90)
        turtle.backward(self._sot)

    def drawEndCircle(self):

        turtle.pencolor('#ff0000') #red
        turtle.width(6)

        turtle.penup()
        turtle.right(90)
        turtle.forward(self._sot)
        turtle.left(90)

        turtle.pendown()
        turtle.circle(self._sot)
        turtle.penup()

        turtle.left(90)
        turtle.forward(self._sot)
        turtle.right(90)
        turtle.backward(self._sot)

    def drawStartCircle(self):
        turtle.pencolor('#009900')  # green
        turtle.width(6)

        turtle.penup()
        turtle.right(90)
        turtle.forward(self._sot)
        turtle.left(90)

        turtle.pendown()
        turtle.circle(self._sot)
        turtle.penup()

        turtle.left(90)
        turtle.forward(self._sot)
        turtle.right(90)
        turtle.backward(self._sot)