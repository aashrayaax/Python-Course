with open("content1.txt","r") as f:
    con1 = f.read()
with open("content2.txt","r") as f:
    con2 = f.read()
if(con1 == con2):
    print("Yes bruh.Content is same")
else:
    print("Nooooo")
