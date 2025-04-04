def greatest():
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    c = int(input("enter a number: "))
    if(a>b and a>c):
        print("a is greatest")
    if(b>a and b>c):
        print("b is greatest")
    if(c>b and c>a):
        print("c is greatest")
greatest()