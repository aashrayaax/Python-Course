f = open("poems.txt","r")
text = f.read()
if("Johny" in text):
    print("Yes")
else:
    print("Nooo")
f.close()