class animals:
    pass
class pets(animals):
    pass
class dogs(pets):
    @staticmethod
    def bark():
        print("BOW BOWWWW")
d = dogs()
d.bark()