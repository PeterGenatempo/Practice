import turtle

def fractal(t, angle, size):
	if size > 10:
		t.left(angle)
		t.forward(size)
		for ang in [45, -45]:
			fractal(t, ang, size/1.2)
		t.left(180)
		t.forward(size)
		t.left(180-angle)

def main():
	t = turtle.Turtle()
	t.speed(0)
	fractal(t, 0, 100)
	t.left(90)
	fractal(t, 0, 100)
	t.left(90)
	fractal(t, 0, 100)
	t.left(90)
	fractal(t, 0, 100)
	t.hideturtle()
	turtle.mainloop()

if __name__ == '__main__':
	main()
