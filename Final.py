from startscreen import *
from coverDesign import *
from build import *
from challenge import *
from learn import *
from checkRamsey import *
from convertNodes import *
from bfs import *
from dfs import *
from visualDFS import *
from visualBFS import *
from cycles import *
from dijkstra import *
from tkinter import *
import random
import math
import copy

def almostEqual(d1, d2, epsilon=10**-7): # taken from class notes
    return (abs(d2 - d1) < epsilon)

def init(data):
    data.startscreen = Startscreen(data)
    data.design1 = Design1(data)
    data.design2 = Design2(data)
    # data.learn = Learn(data)
    data.build = Build(data)
    data.hamilton = Hamilton(data)
    # data.learnBasics = LearnBasics(data)
    # data.searching = Searching(data)
    # data.ramsey = Ramsey(data)
    data.cycles = Cycles(data)
    # data.challenge = Challenge(data)
    # data.level1 = Level1(data)
    # data.level2 = Level2(data)
    # data.level4 = Level4(data)
    # data.level5 = Level5(data)
    data.mode = "startScreen" 
    data.backX = data.width//10-data.width//50
    data.backY = data.height//20
    data.backRX = data.width//15
    data.backRY = data.height//30
    data.nodeR = data.width//80
    data.nodes = dict()
    data.mapNodes = dict()
    data.degrees = dict()
    data.allEdges = dict()
    data.edges = [ ]
    data.redEdges = dict()
    data.blueEdges = dict()
    data.lightNodes = [ ]
    data.numNodes = 0
    data.nextNode = 0
    data.numEdges = 0
    data.nextEdge = 0
    data.highlight = [ ]
    data.erase = [ ]
    data.removedRedEdges = dict()
    data.removedBlueEdges = dict()
    data.lines = [ ]
    data.level = None
    initDijkstra(data)
    initDFS(data)
    data.animateDFS = True
    data.highlightDFS = [ ]
    data.dfs = dfsSearch(graphBuilder(), 0, 7)
    initBFS(data)
    data.animateBFS = True
    data.highlightBFS = [ ]
    data.bfs = bfsSearch(graphBuilder(), 0, 7)
    
# def levelList(data):
#     list = [data.level1, data.level2, data.level4, data.level5]
#     return list
#     
# def checkLevels(canvas, data):
#     levels = levelList(data)
#     for level in levels:
#         if level.win == True:
#             levelNum = levels.index(level)+1
#             # if levelNum < 5:
#             #     canvas.create_rectangle(i*self.dim+self.marginX-self.r,
#             #         j*self.dim+self.marginY-self.r, 
#             #         i*self.dim+self.marginX+self.r,
#             #         j*self.dim+self.marginY+self.r, fill = "lightsteelblue")
#             # data.build.drawCheckmark(canvas, (levelNum-1)*data.challenge.dim+data.challenge.marginX-data.challenge.r
#             #     17, data)

def mousePressed(event, data):
    if data.mode == "startScreen":
        mousePressedStart(event, data)
    # elif data.mode == "learn":
    #     mousePressedLearn(event, data)
    # elif data.mode == "learnBasics":
    #     mousePressedBasics(event, data)
    # elif data.mode == "ramsey":
    #     mousePressedRamsey(event, data)
    # elif data.mode == "searching":
    #     mousePressedSearching(event, data)
    elif data.mode == "cycles":
        mousePressedCycles(event, data)
    elif data.mode == "build":
        mousePressedBuild(event, data)
        data.hamilton.mousePressedHamilton(event, data)
        data.hamilton.chooseStartNode(event, data)
    # elif data.mode == "challenge":
    #     mousePressedChallenge(event, data)
    #     pickLevel(event, data)
    # elif data.mode == "level1":
    #     data.level1.mousePressedTools(event, data)
    #     data.level1.mousePressed(event, data)
    # elif data.mode == "level2":
    #     data.level2.mousePressed(event, data)
    # elif data.mode == "level4":
    #     data.level4.mousePressedTools(event, data)
    #     data.level4.mousePressed(event, data)
    # elif data.mode == "level5":
    #     data.level5.mousePressed(event, data)

def keyPressed(event, data):
    if event.keysym == "n":
        data.build.mode = "node"
    elif event.keysym == "r":
        data.build.mode = "red edge"
    elif event.keysym == "b":
        data.build.mode = "blue edge"
    elif event.keysym == "e":
        data.build.mode = "eraser"
    if data.build.enterWeight == True:
        keyPressedWeight(event, data)

def timerFired(data):
    if data.mode == "startScreen":
        data.design1.timerFired(data)
        data.design2.timerFired(data)
    # if data.mode == "searching":
    #     DFSTimer(data)
    #     BFSTimer(data)
    if data.build.mode == "searchDFS":
        timerDFS(data)
    elif data.build.mode == "searchBFS":
        timerBFS(data)
    
def redrawAll(canvas, data):
    if data.mode == "startScreen":
        canvas.create_rectangle(0,0,data.width, data.height, fill = "sky blue")
        data.design1.redrawAll(canvas, data)
        data.design2.redrawAll(canvas, data)
        data.startscreen.draw(canvas, data)
    # elif data.mode == "learn":
    #     data.learn.draw(canvas, data)
    elif data.mode == "build":
        data.build.draw(canvas, data)
        data.hamilton.drawHamilton(canvas, data)
        redrawBuild(canvas, data)
    # elif data.mode == "challenge":
    #     data.challenge.drawLevels(canvas, data)
    #     checkLevels(canvas, data)
    # elif data.mode == "level1":
    #     data.level1.draw(canvas, data)
    # elif data.mode == "level2":
    #     data.level2.createGraph(canvas, data)
    # elif data.mode == "level4":
    #     data.level4.draw(canvas, data)
    # elif data.mode == "level5":
    #     data.level5.createGraph(canvas, data)
    # elif data.mode == "learnBasics":
    #     data.learnBasics.draw(canvas, data)
    # elif data.mode == "ramsey":
    #     data.ramsey.draw(canvas, data)
    # elif data.mode == "searching":
    #     data.searching.draw(canvas, data)
    #     redrawDFS(canvas, data)
    #     redrawBFS(canvas, data)
    elif data.mode == "cycles":
        data.cycles.draw(canvas, data)
    
####################################
# use the run function as-is
####################################

# taken from class notes

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

run(1000,800)