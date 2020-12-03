import turtle

def fractal(t, n):
	if n < 450:
		t.left(n/2)
		t.forward(n)
		fractal(t, n+1)
	else:
		t.left(n/2)
		t.forward(n/2)

def correctHeading(t):
	head = t.heading()
	t.left(-head)

def newBarb(t, x, y, n):
	t.penup()
	t.goto(x, y)
	t.pendown()
	correctHeading(t)
	fractal(t, n)

def main():
	t = turtle.Turtle()
	t.speed(0)
	newBarb(t, 0, 0, 5)
	newBarb(t, -200, -200, 5)
	newBarb(t, 200, -200, 5)
	newBarb(t, 400, 0, 5)
	newBarb(t, -400, 0, 5)
	newBarb(t, 600, -200, 5)
	newBarb(t, -600, -200, 5)
	newBarb(t, -400, -400, 5)
	newBarb(t, 0, -400, 5)
	newBarb(t, 400, -400, 5)
	newBarb(t, -200, 200, 5)
	newBarb(t, -600, 200, 5)
	newBarb(t, 200, 200, 5)
	newBarb(t, 600, 200, 5)
	t.hideturtle()
	turtle.mainloop()

if __name__ == '__main__':
	main()
