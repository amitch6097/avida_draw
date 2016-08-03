from file_func import*
from draw import*
import glob, os

def main():

    #get input
    work_file = input("Enter single_runs file location:")
    print("ARROW:a")
    print("CIRCLE:c")
    turtleShape = input("TURTLE SHAPE:")

    #get envoirnment file
    env_file = os.path.join(work_file, "env-nav.cfg")

    # move down in directory to find trace file
    os.chdir(os.path.join(work_file, "data","archive"))
    for file in glob.glob("*.trace"):
        trace_file = os.path.join(work_file,"data", "archive", file)

    #move back up in directory ##for saving .eps files
    os.chdir(work_file)

    #get path/grid from files
    files = OpenFiles()
    path = files.openTraceFile(trace_file) #.trace->path->drawPath
    gridList = files.openEnviornmentFile(env_file)#env-nav->grid->drawGrid
    gridLength = files._grid_size

    #Create Screen  - try turtle Shape
    while(True):
        try:
            draw = Draw(gridLength, turtleShape)
            break
        except:
            print("-THAT IS NOT A CORRECT INPUT-")
            print("ARROW:a")
            print("CIRCLE:c")
            turtleShape = input("TURTLE SHAPE:")

    #draw Grid/Path
    # draw.drawGrid(gridList, gridLength)
    draw.drawGrid(gridList)
    turtle.update()

    #input("To start Path press enter")
    draw.drawPath(path, gridList[0], gridLength)
    turtle.done() #makes sure turtle stays open

main()