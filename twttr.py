def main():
    input_String = input("Please input the string you want to shorten: ")
    print(shorten(input_String))


def shorten(word):
    i = 0
    output_String = ""
    while i != len(word):
        next_Character = word[i]
        if not(next_Character.lower() == "a" or next_Character.lower() == "e" or next_Character.lower() == "i" or next_Character.lower() == "o" or next_Character.lower() == "u"):
            output_String = output_String + next_Character
        i += 1
    return output_String


if __name__ == "__main__":
    main()
