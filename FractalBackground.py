from turtle import *
import turtle
import time

def main():
    order = int(input("Order: "))
    size = int(input("Size: "))
    t = turtle.Turtle()
    t.speed(0)
    canvas = Screen()
    canvas.bgcolor("Black")
    t.penup()
    t.left(180)
    t.forward(size / 2)
    t.left(180)
    t.pendown()

    t.showturtle()

    t0 = time.perf_counter()
    loop(t, order, size)
    t1 = time.perf_counter()

    print("---Runtime: {0:.2f} secs---".format(t1-t0))

def loop(t, order, size):
    count = 0
    while count < 1:
        t.fillcolor("Cyan")             #Middle Fractal
        t.begin_fill()
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.fillcolor("Red")
        t.begin_fill()
        t.left(120)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.fillcolor("Red")
        t.begin_fill()
        t.left(60)
        t.right(120)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.penup()
        t.right(180)
        t.forward(size)
        t.pendown()

        t.fillcolor("Red")
        t.begin_fill()
        t.right(120)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.penup()
        t.right(180)
        t.forward(size)
        t.pendown()

        t.fillcolor("Red")
        t.begin_fill()
        t.right(60)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.right(60)

        t.fillcolor("Cyan")             #Right Fractal
        t.begin_fill()
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.fillcolor("Red")
        t.begin_fill()
        t.left(120)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.fillcolor("Red")
        t.begin_fill()
        t.left(60)
        t.right(120)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.penup()
        t.right(180)
        t.forward(size)
        t.pendown()

        t.fillcolor("Red")
        t.begin_fill()
        t.right(120)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.penup()
        t.right(180)
        t.forward(size)
        t.pendown()

        t.fillcolor("Red")
        t.begin_fill()
        t.right(60)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.right(240)
        t.penup()
        t.forward(size * 3)
        t.pendown()
        t.right(180)

        t.fillcolor("Cyan")             #Left Fractal
        t.begin_fill()
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.fillcolor("Red")
        t.begin_fill()
        t.left(120)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.fillcolor("Red")
        t.begin_fill()
        t.left(60)
        t.right(120)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.penup()
        t.right(180)
        t.forward(size)
        t.pendown()

        t.fillcolor("Red")
        t.begin_fill()
        t.right(120)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()

        t.penup()
        t.right(180)
        t.forward(size)
        t.pendown()

        t.fillcolor("Red")
        t.begin_fill()
        t.right(60)
        koch(t, order, size)
        t.right(180)
        koch(t, order, size)
        t.end_fill()


        count += 1

def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
           koch(t, order-1, size/3)
           t.left(angle)

if __name__ == '__main__':
    main()
