from random import randint

invalid_input = True

def start():
	playerScore = 0
	computerScore = 0

	player = input("Pick Rock, Paper, or Scissors:")

	chosen = randint(1 , 3)

	if chosen == 1:
		computer = "Rock"
	elif chosen == 2:
		computer = "Paper"
	else:
		computer = "Scissors"

	print(player, "vs", computer)

	if player == computer:
		print("DRAW!")
		print("Score: Player" , playerScore , "Computer" , computerScore)
	elif player == "Rock" and computer == "Scissors":
		print("Player Wins!")
		playerScore += 1
		print("Score: Player" , playerScore , "Computer" , computerScore)
	elif player == "Rock" and computer == "Paper":
		print("Computer Wins!")
		computerScore += 1
		print("Score: Player" , playerScore , "Computer" , computerScore)
	elif player == "Paper" and computer == "Rock":
		print("Player Wins!")
		playerScore += 1
		print("Score: Player" , playerScore , "Computer" , computerScore)
	elif player == "Paper" and computer == "Scissors":
		print("Computer Wins!")
		computerScore += 1
		print("Score: Player" , playerScore , "Computer" , computerScore)
	elif player == "Scissors" and computer == "Rock":
		print("Computer Wins!")
		computerScore += 1
		print("Score: Player" , playerScore , "Computer" , computerScore)
	elif player == "Scissors" and computer == "Paper":
		print("Player Wins!")
		playerScore += 1
		print("Score: Player" , playerScore , "Computer" , computerScore)

while invalid_input:
	start()
