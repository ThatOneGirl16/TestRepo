import turtle
import random as rand
t = turtle.Pen()
wn = turtle.Screen()


while True:
    R = rand.randrange(10, 50)
    #Start of Code
    t.forward(R)
    t.left(R)
    t.forward(R)
    t.left(R)
    t.forward(R)
    t.left(R)
    t.forward(R)
    #End Code
wn.exitonclick()