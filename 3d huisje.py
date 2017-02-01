import turtle
import math

loop = 1

punten = [[-1,-1,-1],
          [1,-1,-1],
          [1,-1,1],
          [-1,-1,1],

          [-1,1,-1],
          [1,1,-1],
          [1,1,1],
          [-1,1,1]
    ]

gesorteerdepunten = []

locatie = [0,0,2]

cameralocatie = [0,0,0]
richting = 0
camerasnelheid = 0.2
maxcamx = 100

turtle.speed(255)
turtle.tracer(0, 0)

def naarwereldruimte(x,y,z) :
    return x+locatie[0],y+locatie[1],z+locatie[2]

def naarcameraruimte(x,y,z) :
    return x-cameralocatie[0],y-cameralocatie[1],z-cameralocatie[2]

def tekenpunten() :
    for i in range(len(punten)) :
        x1 = punten[i][0]*50
        y1 = punten[i][1]*50
        z1 = punten[i][2]/2

        x1,y1,z1 = naarwereldruimte(x1,y1,z1)
        x1,y1,z1 = naarcameraruimte(x1,y1,z1)

        sx1 = x1/z1
        sy1 = y1/z1

        turtle.goto(sx1,sy1)
        turtle.stamp()

        if i < len(punten) :
    turtle.update()

def camerabeweging() :
    global richting, camerasnelheid, maxcamx
    if cameralocatie[0] < -maxcamx :
        richting = 1
    elif cameralocatie[0] > maxcamx :
        richting = 0
    if richting == 0 :
        cameralocatie[0] = cameralocatie[0] - camerasnelheid
    else :
        cameralocatie[0] = cameralocatie[0] + camerasnelheid

turtle.penup()

while loop == 1 :
    turtle.clear()
    tekenpunten()
    camerabeweging()
