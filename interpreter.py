Input_String = input("Please input the one-digit numbers and the arthematic operator to do calculations: ")
x , y, z = Input_String.split(" ")
if y == "+":
    print(round(float(x) + float(z), 1))
elif y == "-":
    print(round(float(x) - float(z), 1))
elif y == "*":
    print(round(float(x) * float(z), 1))
else:
    print(round(float(x) / float(z), 1))