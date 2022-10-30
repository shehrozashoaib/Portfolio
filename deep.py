StringInput=input("What is the answer to the Great Question of Life, the Universe and Everything?")

if StringInput.lower()== ("forty two") or StringInput.lower()== ("forty-two") or StringInput.strip() == "42":
    print("Yes")
else:
    print("No")



