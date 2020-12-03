def main():
	print("Enter amount followed by first initial of people to split with. ie 4.50 prak or 5.50 pk")
	print("Enter null string to quit")
	response = input("Item: ")

	total = 0
	p_total = 0
	a_total = 0
	r_total = 0
	k_total = 0

	while response != "":
		input_list = response.split()
		total += float(input_list[0])

		if "p" in input_list[1]:
			p_total += float(input_list[0]) / len(input_list[1])

		if "a" in input_list[1]:
			a_total += float(input_list[0]) / len(input_list[1])

		if "r" in input_list[1]:
			r_total += float(input_list[0]) / len(input_list[1])

		if "k" in input_list[1]:
			k_total += float(input_list[0]) / len(input_list[1])

		response = input("Item: ")


	print("Total Cost: $" + str(total))
	print()
	print("Peter Cost: $" + str(p_total))
	print("Ahmed Cost: $" + str(a_total))
	print("Riley Cost: $" + str(r_total))
	print("Kasin Cost: $" + str(k_total))

if __name__ == '__main__':
	main()