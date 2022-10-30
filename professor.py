from random import randint


def main():
    a = get_level()

    score = int(0)
    rounds = int(1)

    while rounds <= 10:
        first_Num = generate_integer(a)
        second_Num = generate_integer(a)
        answer = int(first_Num) + int(second_Num)
        answer_Found = False
        tries = int(0)
        while int(tries) < 3 and not (answer_Found):
            print(str(first_Num), "+", str(second_Num), "=", end=" ")
            user_Answer = input()
            if int(user_Answer) == answer:
                score = score + int(1)
                answer_Found = True
            else:
                print("EEE")
            tries = tries + int(1)
        if answer_Found == False:
            print(str(first_Num), "+", str(second_Num), "=", str(answer))
        rounds = rounds + int(1)

    print("Score: " + str(score))


def get_level():
    correct_Input = False
    input_List = ["1", "2", "3"]

    while not (correct_Input):
        input_Level = input("Level: ")
        if input_Level in input_List:
            correct_Input = True

    return int(input_Level)


def generate_integer(level):
    if int(level) == 1:
        return randint(0, 9)
    if int(level) == 2:
        return randint(10, 99)
    if int(level) == 3:
        return randint(100, 999)


if __name__ == "__main__":
    main()
