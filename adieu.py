import inflect

p = inflect.engine()
b = list()
n = int(0)

try:
    while True:
        b.append(input())
        n += 1
except EOFError:
    pass

my_List = p.join(b)

print("Adieu, adieu, to " + p.join(b))
