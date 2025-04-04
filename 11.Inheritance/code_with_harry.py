class employee:
    a = 1
class student(employee):
    b = 2
class me(student):
    c = 3
# o = employee()
# print(o.b)
o = me()
print(o.a,o.b,o.c)
