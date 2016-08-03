class OpenFiles():

    def __init__(self):
        self._grid_size = 0

    def openTraceFile(self, file):

        for line in reversed(open(file).readlines()):

            if "Ext Mem:" in line:

                splitLine = line.split(", ")
                splitLine = splitLine[10:] #take off front numbers
                splitLine[-1] = splitLine[-1][:-1]

                return splitLine

    def openEnviornmentFile(self, file):

        count = 0
        file = open(file , "r")
        lines = file.readlines()

        grid = []

        #make dictionary with intial x and y as keys, list of lines of letters for each key
        for line in lines:
            count+=1

            if "GRID" in line:

                self._grid_size = int(line[(line.find("height=") + 7):line.find(":", line.find("height="))])
                initx = int(line[(line.find("initx=") + 6):line.find(":", line.find("initx="))])
                inity = int(line[(line.find("inity=") + 6):line.find(":", line.find("inity="))])

                start = (inity*self._grid_size) + initx

                grid.append(start)
                grid.append(lines[count:count+self._grid_size])

                return grid
