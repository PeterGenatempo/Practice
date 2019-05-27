invalid_input = True

def start():
	x = int(input("Number:"))

	if x < 0:
		x = x * -1
		print(x)
	else:
		print(x)

while invalid_input:
	start()
