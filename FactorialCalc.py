invalid_input = True

def start():
	x = int(input("Number:"))

	prod = 1
	num = 1

	if x == 0:
		print("Undefined")

	elif x == 1:
		print(x)

	else:
		while num < x:
			prod = prod * (num+1)
			num =num + 1
		print(prod)

while invalid_input:
	start()
