## parsa badiei


import random
import math

grid = 0
valueF = 0
arrows = 0
def main():
    global grid

    initGrid()
    E_greedy(0.1,0,2,10000)
    print("########## Map ##########")
    for y in range(5):
        print(grid[y])
    return

def initGrid():
    global grid
    global valueF
    global arrows
    valueF = [[0.0 for x in range(7)] for y in range(5)]
    grid = [[' ' for x in range(7)] for y in range(5)]
    arrows = [[' ' for x in range(7)] for y in range(5)]

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

def E_greedy(epsilon,x,y,Steps):
    reward,nextX,nextY,chosenAction = 0,0,0,' '
    alpha , landa = 0.05 , 0.8
    xstart = x
    ystart = y
    for itration in range(Steps):
        terminal = False
        x=xstart
        y=ystart
        while not terminal:
            p = random.random()
            if (p>epsilon):
                chosenAction = choosegreedy(x, y)
                reward, nextX, nextY = applyAction_Greedy(x,y,chosenAction)
            else:
                reward, nextX, nextY, chosenAction = applyAction_nonDeter(x,y,produceAction())

            valueF[y][x] += alpha * (reward + (landa * valueF[nextY][nextX]) - valueF[y][x])
            valueF[y][x] = round(valueF[y][x], 1)
            arrows[y][x] = changeDirToArrow(chosenAction)
            y = nextY
            x = nextX
            if (grid[y][x] == 'W'):
                terminal = True
                arrows[y][x]='W'
            if( grid[y][x] == 'G'):
                terminal = True
                arrows[y][x] = 'G'

        printResults(itration)



def changeDirToArrow(direction):
    dir= { 'R' : '→',
           'L' : '←',
           'U' : '↑',
           'D' : '↓',
           'RU' : '→↑',
           'RD' : '→↓',
           'LU' : '←↑',
           'LD' : '←↓'}
    return dir[direction]
#← ↑ → ↓

def policy(arrow):
    action= {'→' : 'R',
             '←' : 'L',
             '↑' : 'U',
             '↓' : 'D',
             '→↑': 'RU',
             '→↓': 'RD',
             '←↑': 'LU',
             '←↓': 'LD'}
    return action[arrow]



def choosegreedy(xs,ys):
    maxes=[]
    rR , rL , rRU , rRD , rLU, rLD ,rU , rD = applyAction_Greedy(xs, ys, 'R'), applyAction_Greedy(xs, ys, 'L'), applyAction_Greedy(xs, ys, 'RU'), applyAction_Greedy(xs, ys, 'RD'),applyAction_Greedy(xs, ys, 'LU'), applyAction_Greedy(xs, ys, 'LD'), applyAction_Greedy(xs, ys, 'U'), applyAction_Greedy(xs, ys, 'D')

    rewardsDictionary = {'R' : valueF[rR[2]][rR[1]]  , 'L':valueF[rL[2]][rL[1]] ,'U':valueF[rU[2]][rU[1]] , 'D':valueF[rD[2]][rD[1]], 'RU':valueF[rRU[2]][rRU[1]] , 'RD':valueF[rRD[2]][rRD[1]] , 'LU':valueF[rLU[2]][rLU[1]], 'LD':valueF[rLD[2]][rLD[1]] }
    GreedyAction = max(rewardsDictionary, key=rewardsDictionary.get)
    maxes.append(GreedyAction)
    for key in rewardsDictionary:
        if(rewardsDictionary[key] == GreedyAction):
            maxes.append(rewardsDictionary[key])
    i = int ( random.random() * len(maxes))
    print(maxes[i])
    return maxes[i]

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

def applyAction_nonDeter(xs, ys, a):
    global grid
    state = {
        'W': -250,
        ' ': -1,
        'G': 1000,
        'S': -1
    }

    xtemp , ytemp = xs, ys
    chosen_action = ''
    rnd = random.random()
    if (a =='R'):
        if(rnd>0.2 ):
            xtemp = xs + 1
            chosen_action='R'
        elif(rnd<0.1):
            xtemp = xs + 1
            ytemp = ys + 1
            chosen_action= 'RD'
        else:
            xtemp = xs + 1
            ytemp = ys - 1
            chosen_action='RU'
    elif( a =='RU'):
        if(rnd>0.2 ):
            xtemp = xs + 1
            ytemp = ys -1
            chosen_action='RU'
        elif(rnd<0.1):
            ytemp = ys - 1
            chosen_action='U'
        else:
            xtemp = xs + 1
            chosen_action='R'
    elif( a=='RD'):
        if(rnd>0.2 ):
            xtemp = xs + 1
            ytemp = ys + 1
            chosen_action='RD'
        elif(rnd<0.1):
            xtemp = xs + 1
            chosen_action='R'
        else:
            ytemp = ys + 1
            chosen_action='D'

    if (ytemp > 4):
        ytemp -=1
    if(ytemp<0):
        ytemp +=1
    if(xtemp >6):
        xtemp-=1
    # x<0 is not nessecary because there is no action to cause that
    return state[grid[ytemp][xtemp]],xtemp,ytemp,chosen_action

def applyAction_Greedy(xs, ys, a):
    global grid
    state = {
        'W': -250,
        ' ': -1,
        'G': 1000,
        'S': -1
    }

    xtemp , ytemp = xs, ys

    if (a =='R'):
        xtemp = xs + 1
    elif( a =='RU'):
        xtemp = xs + 1
        ytemp = ys -1
    elif( a=='RD'):
        xtemp = xs + 1
        ytemp = ys + 1
    elif (a == 'L'):
        xtemp = xs - 1
    elif (a == 'U'):
        ytemp = ys - 1
    elif (a == 'D'):
        ytemp = ys + 1
    elif (a == 'LD'):
        ytemp = ys + 1
        xtemp = xs - 1
    elif (a == 'LU'):
        ytemp = ys - 1
        xtemp = xs - 1


    offgrid = False
    if (ytemp > 4):
        ytemp -=1
    if(ytemp<0):
        ytemp +=1
    if(xtemp >6):
        xtemp-=1
    if(xtemp < 0):
        xtemp+=1

    return state[grid[ytemp][xtemp]],xtemp,ytemp


def printResults(x):
    print( " ---------------","Episode: ", x + 1, " ---------------")
    for y in range(5):
        for x in range(7):
            print(valueF[y][x], "\t|\t", end='')
        print()
    print(" \t------------------------------")
    for y in range(5):
        for x in range(7):
            print(arrows[y][x], "\t|\t", end='')
        print()

    return
main()
input()

