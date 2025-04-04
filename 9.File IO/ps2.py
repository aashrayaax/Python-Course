import random
def game():
    score = random.randint(1,100)
    f=open("hiscore.txt","r")
    hiscore = f.read()
    f.close()
    if(hiscore==""):
        f=open("hiscore.txt","w")
        hiscore = f.write("score")
        f.close()
    elif(int(hiscore)<int(score)):
        f=open("hiscore.txt","w")
        hiscore = f.write("score")
        f.close()
game()

    
