import random

print("=====================")
print("ROCK-PAPER-SCISSORS")
print("=====================")

while True:
    #options for the user
    print("\n1) ✊\n2) ✋\n3) ✌️\n4) Quit")

    #player's choice
    x = int(input("Pick a number: "))

    #quit condition
    if x == 4:
        print("Thanks for playing! Goodbye 👋")
        break

    #validity
    if x not in [1, 2, 3]:
        print("Invalid choice! Please pick 1, 2, 3, or 4 to quit.")
        continue

    #computer's choice
    y = random.randint(1, 3)

    #mapping 
    choices = {1: "✊", 2: "✋", 3: "✌️"}
    player = choices[x]
    cpu = choices[y]

    #display choices
    print(f"\nYou chose: {player}")
    print(f"CPU chose: {cpu}")

    #deciding conditions for winner
    if x == y:
        print("It's a tie! Play again.")
    elif (x == 1 and y == 3) or (x == 2 and y == 1) or (x == 3 and y == 2):
        print("🎉 You won!!")
    else:
        print("😢 You lost!!")



