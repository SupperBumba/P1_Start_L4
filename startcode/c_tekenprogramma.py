import turtle

turtle.showturtle()

turtle.left(90)

def move_up():
    turtle.forward(50)
def move_left():
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
def move_right():
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
def move_down():
    turtle.left(180)
    turtle.forward(50)
    turtle.left(180)
def pen_up():
    turtle.penup()
def pen_down():
    turtle.pendown()

while True:
    move = input()
    if move == 'up':
        move_up()
    if move == 'left':
        move_left()
    if move == 'right':
        move_right()
    if move == 'down':
        move_down()
    if move == 'pu':
        pen_up()
    if move == 'pd':
        pen_down()
    if move == 'stop':
        break

turtle.done()