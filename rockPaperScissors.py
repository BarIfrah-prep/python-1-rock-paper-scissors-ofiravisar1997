# Rock Paper Scissors
# A code file structure:
# A line that starts with "#"  is a comment line (it will not be interpreted)
"""
If you ant to comment multiple lines, start and finish with three (3) double quotes (")
As you can see, this line is also a comment.

"""

# ----------------------------------------------------------------------------------------------------------------------
# Here you include all of your package imports (like randome and time packages wev'e discussed about) 
# ----------------------------------------------------------------------------------------------------------------------
import random

# ----------------------------------------------------------------------------------------------------------------------
# Here you will write all of the functions (for later stages of the course
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Here you write code :)
# ----------------------------------------------------------------------------------------------------------------------
"""
I'll give you the text inputs for this program, to make your lives a little easier.
In addition, and to make it simple to you, the input from the user will be an integer:
1 for ROCK
2 for PAPER
3 for SCISSORS
A text input describing the operation is unacceptable and will cost you with points.

A quick reminder of the rules:

ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins
SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win
PAPER(2) vs ROCK(1)      --> PAPER(2) wins

DO NOT ADD EXTRA OPTIONS (No lizard, no Spock.)
"""

gameIsOn = True
userWinsCount = 0
computerWinsCount = 0
userName = input("Welcome to the game ! please enter your name ?")
print(f"Hello {userName}")
# print the instructions for the user to see:
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")

# The game will run in a WHILE loop.
# The loop is infinite, and only the user has the power to stop it (when they say they don't want to play anymore)
while gameIsOn:
        userChoice = input("Choose Your Choice Rock(1),Paper(2),Scissors(3)")

        while userChoice != "1" and userChoice != "2" and userChoice != "3":

        # User Choice is Invalid
            print("Not a valid Choice.\n Choose again!")
            userChoice = input("Choose Your Choice Rock(1),Paper(2),Scissors(3)")
        else:
            # User Choice Is Valid
            computerChoice = random.randint(1, 3)
            userChoice = int(userChoice)

            # User Choice Rock
            if userChoice == 1 and computerChoice == 3:
                print("Computer choice: Scissors")
                print("Your choice: Rock \nYou won!")
                userWinsCount += 1
                print(f"Your wins count is {userWinsCount}")
            elif userChoice == 1 and computerChoice == 2:
                print("Computer choice: Paper")
                print("Your choice: Rock \nYou lost!")
                computerWinsCount += 1
                print(f"Computer wins count is {computerWinsCount}")
            elif userChoice == 1 and computerChoice == 1:
                print("You both choose rock its draw!")

            # User Choice Scissors

            if userChoice == 3 and computerChoice == 2:
                print("Computer choice: Paper")
                print("Your choice: Scissors \nYou won!")
                userWinsCount += 1
                print(f"Your wins count is {userWinsCount}")
            elif userChoice == 3 and computerChoice == 1:
                print("Computer choice: Rock")
                print("Your choice: Scissors \nYou lost!")
                computerWinsCount += 1
                print(f"Computer wins count is {computerWinsCount}")
            elif userChoice == 3 and computerChoice == 3:
                print("You both choose Scissors its draw!")

            # User Choice Paper

            if userChoice == 2 and computerChoice == 1:
                print("Computer choice: Rock")
                print("Your choice: Paper \nYou won!")
                userWinsCount += 1
                print(f"Your wins count is {userWinsCount}")
            elif userChoice == 2 and computerChoice == 3:
                print("Computer choice: Scissors")
                print("Your choice: Paper \nYou lost!")
                computerWinsCount += 1
                print(f"Computer wins count is {computerWinsCount}")
            elif userChoice == 2 and computerChoice == 2:
                print("You both choose paper its draw!")

        continueAnswer = input("Wanna continue ? y/n")
        continueRequest = True

        while continueRequest:
            if continueAnswer.lower() == "n":
                print("Thanks for playing !")
                gameIsOn = False
                continueRequest = False
            elif continueAnswer.lower() == "y":
                print("Lets continue the game!")
                continueRequest = False
            else:
                print("Invalid answer!")
                continueAnswer = input("Wanna continue ? y/n")

