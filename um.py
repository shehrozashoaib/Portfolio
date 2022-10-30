import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    return_Val = int(0)
    matches = re.findall(r"\b(um)\b",s,re.IGNORECASE)
    if matches:
        print(matches)
        return_Val = len(matches)
        return return_Val
    return return_Val






if __name__ == "__main__":
    main()