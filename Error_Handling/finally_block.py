try:
    f=open("texts.txt","r")
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File is not present")
finally:
    print("Closing without finding the file")