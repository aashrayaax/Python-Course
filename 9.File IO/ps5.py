words = ["fucking","perverty", "bitch","sassy"]

with open("censor.txt","r") as f:
    content = f.read()
for word in words:
    content = content.replace(word,"*"*len(word))
with open("censor.txt","w") as f:
    f.write(content)

