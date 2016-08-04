from draw_func import*

class Draw:

    def __init__(self, givenSize, shape):

        if (shape == "a"):
            turtle.shape('classic')
            turtle.shapesize(2, 2, 5)
        elif(shape == "c"):
            turtle.shape('circle')
            turtle.shapesize(.75 ,.75 ,1)
        else:
            raise Exception

        self._sot = int((25/givenSize)*8)
        self._symbols = DrawSymbols(self._sot)

        #intial turtle locations
        self._x = -620
        self._y = 327

        #store last position
        self._lastx = -1
        self._lasty = -1

        #window size
        turtle.setup(1280, 692)  # half 640, 347 #padding 20px #620,327

        turtle.tracer(0,0)
        turtle.speed(0) #turtle speed 0:fastest 1-9:slow to fast
        turtle.hideturtle() #turtle is invisible (might speed up drawing)

        # go to start position
        turtle.penup()
        turtle.goto(self._x , self._y)
        turtle.pendown()
        turtle.update()

    def drawPath(self, path, start, gridLength):

        turtle.tracer(1,10)
        #turtle.speed(0)
        turtle.st()

        path.insert(0, start)


        # get bottom of the grid
        xzero = self._x + (self._sot / 2)
        yzero = (self._y - ((gridLength-1) * self._sot * 3) + (self._sot / 2))
        turtle.penup()

        turtle.pencolor("black")
        turtle.fillcolor("black")
        turtle.pensize(1)
        lastnum = 0

        for s in path:
            # each number is a string
            num = int(s)
            self.getDirection(lastnum - num, gridLength)

            #do math to find next position
            #75 should give the cordinates (0,3)
            movex = num % gridLength
            movey = num / gridLength
            movey = int(movey)

            #prevent the wrap around effect from drawing a line across the screen
            if abs(movex - self._lastx) == (gridLength - 1) or abs(movey - self._lasty) == (gridLength - 1):
                turtle.penup()

            #move to new location
            turtle.goto((movex * self._sot * 3) + xzero, (movey * self._sot * 3) + yzero)

            if (s == path[0]): self._symbols.drawStartCircle()
            # drawStart changes pen
            turtle.pencolor("black")
            turtle.pensize(1)
            turtle.pendown()
            lastnum = num

        self._symbols.drawEndCircle()

        #get picture, .eps file, from screen for path
        turtle.ht()
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file="path.eps")


    def drawGrid(self, grid):

        # used for creating newLine()
        ytemp = self._y

        #start  = grid[0]
        grid = grid[1]

        for line in grid:

            # to offset newLine()
            ytemp -= (self._sot * 3)
            for letter in line:

                if (letter == ","):
                    self._symbols.drawSpace()
                if (letter == "o"):
                    self._symbols.drawX()
                if (letter == "R"):
                    backgroundColorForTurn = '#d09fff'
                    self._symbols.drawCircleRight(backgroundColorForTurn)
                if (letter == "L"):
                    backgroundColorForTurn = '#ffff48'
                    self._symbols.drawCircleLeft(backgroundColorForTurn)
                if (letter == "N"):
                    self._symbols.drawNutrient2()
                if (letter == "E"):
                    self._symbols.drawE()
                if (letter == "S"):
                    self._symbols.drawE()
            self._symbols.newLine(ytemp)

        ts = turtle.getscreen()
        # name it based on grid intial x and y
        ts.getcanvas().postscript(file="grid.eps")

    def getDirection(self, num, gridLength):
        if (num == 1):
            turtle.setheading(180)
        if (num == ((0 - gridLength) - 1)):
            turtle.setheading(45)
        if (num == (0 - gridLength)):
            turtle.setheading(90)
        if (num == ((0 - gridLength) + 1)):
            turtle.setheading(135)
        if (num == -1):
            turtle.setheading(0)
        if (num == (gridLength + 1)):
            turtle.setheading(225)
        if (num == gridLength):
            turtle.setheading(270)
        if (num == (gridLength - 1)):
            turtle.setheading(315)
