a = {"Quantity":[],"Name":[]}
b = list(a.values())
item_Name = b[0]
item_Quantity = b[1]
try:
    while True:
        item = input()
        item = item.upper()
        if item in item_Name:
            ind = item_Name.index(item)
            item_Quantity[ind] = int(item_Quantity[ind]) + int(1)
        else:
            item_Name.append(item)
            item_Quantity.append(1)
except (EOFError,KeyError,ValueError):
    pass
item_Name.sort()
for i in range(len(item_Name)):
    print(item_Quantity[i] , item_Name[i])
