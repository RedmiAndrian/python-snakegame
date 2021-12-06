import os
import time
import keyboard
import curses
import random

grid = [[ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]


#stupid programmer's variable 
apple_pos = (-1, -1)

# stupid booleans
apple_Spawned = False
apple_Eaten = False


# function to draw grid
def draw():
    for i in grid:
        print(i)


# list for the snake body and turning point
body = [(5,5), (4,5), (3,5)]

# direction of the snake
dir = "DOWN"

# initial snake position
head_pos_x = body[0][1]
head_pos_y = body[0][0]


# point/length of the snake
point = 0

# function to place apple on the grid map
def spawn_apple():
    global apple_Spawned
    global apple_Eaten
    global apple_pos
    apple_x = random.randint(0, 9)
    apple_y = random.randint(0, 9)
    if (apple_y, apple_x) not in body and apple_Spawned == False:
        grid[apple_x][apple_y] = "A"
        apple_pos = (apple_y, apple_x)
        apple_Spawned = True
        apple_Eaten = False

def check_apple():
    global apple_pos
    global apple_Eaten
    global apple_Spawned
    if (apple_Eaten == True or apple_Spawned == False) and apple_pos == (-1, -1):
        spawn_apple()

# reinit the variable of the position of the snake in the grid and the grid itself
def reinit_grid():
    global grid
    grid = [[ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
    if apple_pos != (-1, -1):
        grid[apple_pos[0]][apple_pos[1]] = "A"

def reinit(): 
    global grid
    reinit_grid()
    for i in body:
        pos_x = i[1]
        pos_y = i[0]
        grid[pos_y][pos_x] = "#"
    
    for i in grid:
        print(i)


# function to update the position of the head in the grid
def update_snake_body(x, y):
    global apple_Spawned
    global apple_pos
    global apple_Eaten
    if grid[y][x] == "A":
        apple_Eaten = True   
    body.insert(0, (y, x))
    # check if the apple is eaten, if it's eaten, then delay the body.pop by one :)
    if apple_Eaten == False:
        body.pop()
    elif apple_Eaten == True:
        apple_Spawned = False
        apple_pos = (-1, -1)
    print()
    print(body)
    print()
    reinit()
     

# function to move the snake in the grid/map
def head_move(direction, x, y):
    tx = x
    ty = y
    if direction == "UP":
        ty = ty - 1
    if direction == "DOWN":
        ty = ty + 1
    if direction == "LEFT":
        tx = tx - 1
    if direction == "RIGHT":
        tx = tx + 1
    update_snake_body(tx, ty)

while True:
    check_apple()
    head_pos_y = body[0][0]
    head_pos_x = body[0][1]
    if keyboard.is_pressed("up") and dir != "DOWN":
        dir = "UP"
    if keyboard.is_pressed("left") and dir != "RIGHT":
        dir = "LEFT"
    if keyboard.is_pressed("right") and dir != "LEFT":
        dir = "RIGHT"
    if keyboard.is_pressed("down") and dir != "UP":
        dir = "DOWN"    
    time.sleep(1)
    head_move(dir, head_pos_x, head_pos_y)
    print()
    print(dir)
    #draw()
