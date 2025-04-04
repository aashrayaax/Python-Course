with open("log.txt","r") as f:
    content = f.read()
if "python" in content:
    print("yes bruh.python is present")
else:print("noooooo")