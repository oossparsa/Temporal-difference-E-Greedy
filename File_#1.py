## parsa badiei

import random
grid = 0
valueF = 0
def main():
    global grid

    initGrid()
    TDZero(1000)
    print("########## Map ##########")
    for y in range(5):
        print(grid[y])
    return

def initGrid():
    global grid
    global valueF
    valueF = [[0.0 for x in range(7)] for y in range(5)]
    grid = [[' ' for x in range(7)] for y in range(5)]

    grid[0][3] = 'W'
    grid[0][4] = 'W'
    grid[0][5] = 'W'
    grid[0][6] = 'W'

    grid[1][6] = 'W'

    grid[2][0] = 'S'
    grid[2][2] = 'W'
    grid[2][4] = 'W'
    grid[2][6] = 'G'

    grid[3][1] = 'W'
    grid[3][2] = 'W'
    grid[3][5] = 'W'

    grid[4][3] = 'W'
    grid[4][4] = 'W'
    grid[4][5] = 'W'

    return

def produceAction():

    p = random.random()
    if(p<0.5):
        return 'R'
    else:
        p2 = random.randint(0,1)
        action= {
            0 : 'RU',
            1 : 'RD'
        }

    return action[p2]

def applyAction(xs,ys,a):
    global grid
    state = {
        'W': -250,
        ' ': -1,
        'G': 1000,
        'S': -1
    }

    xtemp , ytemp = xs, ys

    rnd = random.random()
    if (a =='R'):
        if(rnd>0.2 ):
            xtemp = xs + 1
        elif(rnd<0.1):
            xtemp = xs + 1
            ytemp = ys + 1
        else:
            xtemp = xs + 1
            ytemp = ys - 1
    elif( a =='RU'):
        if(rnd>0.2 ):
            xtemp = xs + 1
            ytemp = ys -1
        elif(rnd<0.1):
            ytemp = ys - 1
        else:
            xtemp = xs + 1
    elif( a=='RD'):
        if(rnd>0.2 ):
            xtemp = xs + 1
            ytemp = ys + 1
        elif(rnd<0.1):
            xtemp = xs + 1
        else:
            ytemp = ys + 1

    if(grid[ys][xs]=='G'):
        return 1000,xs,ys

    offgrid = False
    if (ytemp > 4):
        ytemp -=1
    if(ytemp<0):
        ytemp +=1
    if(xtemp >6):
        xtemp-=1
    # x<0 is not nessecary because there is no action to cause that
    return state[grid[ytemp][xtemp]],xtemp,ytemp

def TDZero(i):
    global valueF
    alpha = 0.05
    landa = 0.8
    reward=0
    XPrime = 0
    YPrime = 0
    for x in range(i):
        xS = 0
        yS = 2
        terminal = False
        while not terminal:
            reward , XPrime , YPrime = applyAction(xS,yS,produceAction())
            valueF[yS][xS] += alpha*(reward + (landa*valueF[YPrime][XPrime]) - valueF[yS][xS])
            valueF[yS][xS] = round(valueF[yS][xS],1)
            yS = YPrime
            xS = XPrime
            if(grid[yS][xS] == 'W' or grid[yS][xS] == 'G'):
                terminal = True
                printResults(x)
    return


def printResults(x):
    print( " ---------------","Episode: ", x + 1, " ---------------")
    for y in range(5):
        for x in range(7):
            print(valueF[y][x], "\t|\t", end='')
        print()


    return
main()
input()

