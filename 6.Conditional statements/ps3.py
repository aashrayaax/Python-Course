a = input("Enter paragraph: ")
p1 = "Make a lot of money"
p2 = "Buy our product"
p3 = "Do you want to become rich"
p4 = "click this link"
if((p1 in a) or (p2 in a) or (p3 in a) or (p4 in a)):
    print("This is a fraud message")
else:
    print("This is not fraud.This can be trust worthy")   