from random import randint

level_Verified = True

while level_Verified:
    upper_Boundary = input("Level: ")
    if upper_Boundary.isdigit() and int(upper_Boundary) > 0:
        level_Verified = False

rand_Num = int(randint(1, int(upper_Boundary)))
correct_Guess = False

while not (correct_Guess):
    try:
        player_Guess = input("Guess: ")
        if player_Guess.isdigit() and int(player_Guess) > 0:
            if int(player_Guess) == rand_Num:
                print("Just right!")
                correct_Guess = True
            if int(player_Guess) > rand_Num:
                print("Too large!")
            if int(player_Guess) < rand_Num:
                print("Too small!")
    except ValueError:
        pass
