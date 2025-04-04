class employee:

    company = "amazon"
    def show(self):
        print(f"The name is {self.name} and his salary is {self.salary}")
class programmer(employee):
    company = "TCS"
    # def show(self):
    #     print(f"The name is {self.name} and his salary is {self.salary}")
    def showy(self):
        print(f"I just wrote this to tell you that {self.language} is my favourite language")
a = employee()
b = programmer()
print(a.company,b.company)