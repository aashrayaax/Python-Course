# try:
#     a = int(input("Enter : "))
#     print(a)
# except Exception as e:
#     print(e)


a = int(input("Enter 1st number"))
b = int(input("Enter 2st number"))

if(b == 0):
    raise ZeroDivisionError("Bruhhhh U cant divide a number with 0 kadhaa .so vere number ivvu bruhh")
else:
    print(f"The answer is {a/b}")

