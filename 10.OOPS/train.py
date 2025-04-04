from random import randint
class train:
    def __init__(self,trainno):
        self.trainno = trainno
    def book(self, fro, to):
        print(f"The train no is {self.trainno} its from {fro} to {to}")
    def getstatus(self):
        print(f"The train no is {self.trainno} is on time")
    def getfare(self,fro,to):
         print(f"The train no is {self.trainno} its from {fro} to {to} and fare is {randint(222,856)}")
t = train(125354)
t.book("rampur","delhi")
t.getfare("rampur","delhi")
t.getstatus()
