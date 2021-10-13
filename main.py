from random import randint

#create a list of play options
rps = ["ROCK", "PAPER", "SCISSORS"]

#assign a random play to the computer
computerChoice = randint(0,2)

def playAgain():
  playAgain = "z"
  while playAgain != "Y" and playAgain != "N":
    playAgain = input("Do you want to play again? \n Y or N   ")
    if type(playAgain) == str:
      playAgain = playAgain.upper()
    if playAgain == "Y":
      return(True)
    elif playAgain == "N":
      return(False)

#set player to False
play = True

while play:

  playerChoice = input("Enter choice: Rock, Paper, Scissors - ")

  if type(playerChoice) == str:
    playerChoice = playerChoice.upper()

  else:
    print("Sorry your entry wasn't accepted, try again")


  if playerChoice == rps[computerChoice]:
    print("Tie Game!  " + playerChoice + " vs " + rps[computerChoice])

  if playerChoice == "ROCK":
    if computerChoice == 1:
      print("You Lose:  " + playerChoice + " vs " + rps[computerChoice])
    elif computerChoice == 2:
      print("You win:  " + playerChoice + " vs " + rps[computerChoice])

  elif playerChoice == "PAPER":
    if computerChoice == 0 :
      print("You Win:  " + playerChoice + " vs " + rps[computerChoice])
    elif computerChoice == 2:
      print("You Lose:  " + playerChoice + " vs " + rps[computerChoice])

  elif playerChoice == "SCISSORS":
    if computerChoice == 0 :
      print("You Lose:  " + playerChoice + " vs " + rps[computerChoice])
    elif computerChoice == 1:
      print("You Win:  " + playerChoice + " vs " + rps[computerChoice])

  elif playerChoice == "SNAKE" or playerChoice == "PYTHON":
    print("Your the king of Rock, Paper, Scissors!!")

  elif playerChoice == "SHOE":
    print("You wi...\nWhy would you play with a Shoe? Then again Rocks and Scissors aren't toys either...what kind of a game is this!! I quit!")
    quit()

  play = playAgain()



