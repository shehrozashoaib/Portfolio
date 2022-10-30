input_String = input("Please input the string you want to convert to snake case: ")
i = 0
output_String = ""
while i != len(input_String):
    next_Character = input_String[i]
    if next_Character.isupper():
        output_String = output_String + "_" + next_Character.lower()
    else:
        output_String = output_String + next_Character
    i += 1
print(output_String)

