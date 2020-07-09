import math
def createGrid():
    grid = []
    for i in range(21):
        row = []
        for j in range(21):
            if(i==10):
                if(j==10):
                    row.append('+')
                else:
                    row.append('-')
            else:
                if(j==10):
                    row.append('|')
                else:
                    row.append(' ')                
        grid.append(row)
    return grid

def populateGrid(equation,grid):
    for x in range(-10,11):
        y = round(eval(equation))
        if(y>=-10 and y <=10):
            grid[10-y][x+10] = "*"
    
    return grid

def printGrid(grid):
    for i in grid:
        for j in i:
            print(j,end='')
        print()

printGrid(populateGrid(input('Enter a function f(x):\n'),createGrid()))