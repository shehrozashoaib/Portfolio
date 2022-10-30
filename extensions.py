File_Name = input("Please enter the name of the file to check the media type: ")
File_Name = File_Name.strip()
if File_Name[-4:].lower() == ".gif":
    print("image/gif")
elif File_Name[-4:].lower() == ".jpg" or File_Name[-5:].lower() == ".jpeg":
    print("image/jpeg")
elif File_Name[-4:].lower() == ".png":
    print("image/png")
elif File_Name[-4:].lower() == ".pdf":
    print("application/pdf")
elif File_Name[-4:].lower() == ".txt":
    print("text/plain")
elif File_Name[-4:].lower() == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")
