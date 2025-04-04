class employee:
    company = "amazon"
    name = "Ashu"
    def show(self):
        print(f"The name is {self.name} and his company is {self.company}")
class programmer(employee):
    language = "JAVA"
    name = "default name"
    # def show(self):
    #     print(f"The name is {self.name} and his salary is {self.salary}")
    def showy(self):
        print(f"I just wrote this to tell you that {self.language} is my favourite language and my name is {self.name}")
class coder(programmer):
    language = "Python"
    def com(self):
        print(f"The only language which I know is {self.language}")
a = employee()
b = programmer()
c = coder()
# print(a.company,b.company,c.language)
b.show()
c.com()
b.showy()