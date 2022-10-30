loop_Continue = False
can_Charges = int(50)
amount_Paid = int(0)
while not (bool(loop_Continue)):
    input_Amount = int(
        input("Please input the coin: ")
    )
    if input_Amount == 25 or input_Amount == 10 or input_Amount == 5:
        amount_Paid = int(amount_Paid) + int(input_Amount)
        amount_Due = can_Charges - amount_Paid
        if amount_Due <= 0:
            Change = int(amount_Paid) - 50
            print("Change owed: " + str(Change))
            loop_Continue = True
        else:
            print("Amount due: " + str(amount_Due))
    else:
        print("Amount due: " + str(int(can_Charges - amount_Paid)))
