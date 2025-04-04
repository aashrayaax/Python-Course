class employee:
    company = "amazon"
    name = "default name"
    def show(self):
        print(f"The name is {self.name} and his company is {self.company}")
class coder:
    language = "Python"
    def com(self):
        print(f"The only language which I know is {self.language}")
class programmer(employee,coder):
    company = "TCS"
    # def show(self):
    #     print(f"The name is {self.name} and his salary is {self.salary}")
    def showy(self):
        print(f"I just wrote this to tell you that {self.language} is my favourite language")
a = employee()
b = programmer()
# c = coder()
# print(a.company,b.company)
b.show()
b.com()
b.showy()
# print(a.company,b.company)


