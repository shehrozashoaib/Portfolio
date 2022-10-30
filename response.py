from validators import email


x = (lambda s : email(s))

if x(input("Email: ")):
    print("Valid")
else:
    print("Invalid")





