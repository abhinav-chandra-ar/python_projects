import random

print("=====================")
print("ROCK-PAPER-SCISSORS")
print("=====================")

#options for the user
print("1) ✊\n2) ✋\n3) ✌️")

#player's choice
x = int(input("Pick a number: "))

#validity
if x not in [1, 2, 3]:
    print("Invalid choice! Please pick 1, 2, or 3.")
else:
    #computer's choice
    y = random.randint(1, 3)

    #mapping 
    if x == 1:
        player = "✊"
    elif x == 2:
        player = "✋"
    else:
        player = "✌️"

    if y == 1:
        cpu = "✊"
    elif y == 2:
        cpu = "✋"
    else:
        cpu = "✌️"

    #display choices
    print(f"You chose: {player}")
    print(f"CPU chose: {cpu}")

    #deciding conditions for winner
    if x == y:
        print("No Result, play again!!")
    elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
        print("The player won!!")
    else:
        print("The player lost!!")





