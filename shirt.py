import sys
from PIL import (Image,ImageOps)


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif (
    (sys.argv[1].lower().endswith(".jpeg") and sys.argv[2].lower().endswith(".jpeg"))
    or (sys.argv[1].lower().endswith(".jpg") and sys.argv[2].lower().endswith(".jpg"))
    or (sys.argv[1].lower().endswith(".png") and sys.argv[2].lower().endswith(".png"))
):
    try:
        shirt = Image.open("shirt.png")
        user_image = Image.open(sys.argv[1])
        size = shirt.size
        new_copy = ImageOps.fit(user_image,size)
        new_copy.paste(shirt, shirt)
        new_copy.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")
elif (
    not (sys.argv[1].endswith(".jpeg"))
    or not (sys.argv[1].endswith(".jpg"))
    or not (sys.argv[1].endswith(".png"))
    or not (sys.argv[2].endswith(".jpeg"))
    or not (sys.argv[2].endswith(".jpg"))
    or not (sys.argv[2].endswith(".png"))
):
    sys.exit("Invalid output")
else:
    sys.exit("Input and output have different extensions")
