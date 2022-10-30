def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    alpha_Count = int(0)
    num_Count = int(0)
    first_Num_Count = int(0)
    condition_Nullified = True
    verified = False
    if len(s) >= 2 and len(s) <= 6:
        if s.isalnum():
            i = 0
            while i != (len(s)):
                if s[i].isalpha():
                    alpha_Count = alpha_Count + 1
                if (
                    s[i].isnumeric()
                    and first_Num_Count == 0
                    and int(s[i]) != 0
                    and num_Count == 0
                ):
                    first_Num_Count = int(1)
                if s[i].isnumeric():
                    num_Count = num_Count + int(1)
                if s[i].isalpha() and first_Num_Count == 1:
                    condition_Nullified = False
                i += 1
            if first_Num_Count == 1 and condition_Nullified and alpha_Count >= 2:
                verified = True
            elif alpha_Count >= 2 and num_Count == 0 and (condition_Nullified):
                verified = True
    return verified


main()
