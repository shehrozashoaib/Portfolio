d = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = int(0)

try:
    while True:
        item = input("Item: ")
        if item.title() in d:
            total = total + d[item.title()]
            print(f"Total: " + "$" + str("{:.2f}".format(total)))
except (EOFError,KeyError):
    pass

print('\n')