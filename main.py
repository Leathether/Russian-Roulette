import random

chips = 20

def black_red(chips):
    if chips == 0: return
    guess = input("black or red?:  ")
    bet = int(input("how much to bet?:  "))
    while(bet > chips):
        print("you do not have enough chips")
        bet = int(input("how much to bet?:  "))
    actual = random.randint(0,1)
    if ((actual == 0) and (guess == 'red')) or ((actual == 1) and (guess == 'black')):
        chips = chips +  bet
        print(f"You win. Chips: {chips}")
    else:
        chips = chips - bet
        print(f"You lose. Chips: {chips}")

    black_red(chips)

black_red(chips)
