class ClassName():
    def __init__(self, param1):
        self.param1 = param1 
        print('object created')
    def say_hello(self):
        print(f"heloo")
        
        
class Circle():
    pi = 3.1415926
    def __init__(self, r):
        self.r = r 
    def masahat(self):
        m = self.r * self.r * Circle.pi
        return m 
c1 = Circle(10)
print(c1.masahat())


class Person:
    def say_hello(self):
        return "hello"

p = Person()
print(p.say_hello())



class Book():
    def __init__(self, name, page):
        self.pages = page
        self.name = name

        
    def open(self):
        print(f"opened the {self.name} which has {self.page} pages")

class Darsi(Book):
    def __init__(self, name, page, reshte, paye):
        Book.__init__(self, name, page)
        print('a new darsi book')
        self.reshte = reshte
        self.paye = paye
    def open(self):
        print(f"opened {self.name} of {self.reshte} paye {self.paye} ")

d = Darsi('tajrobi', 3, '300 nokte', 120)
d.open()