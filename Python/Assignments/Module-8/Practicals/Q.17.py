# Q.17 Write a Python program to show hybrid inheritance. 

class Base:
    def show_base(self):
        print("Base class")

class Derived1(Base):
    def show_derived1(self):
        print("Derived 1 class")

class Derived2(Base):
    def show_derived2(self):
        print("Derived 2 class")

class Hybrid(Derived1, Derived2):
    def show_hybrid(self):
        print("Hybrid class")

obj = Hybrid()
obj.show_base()
obj.show_derived1()
obj.show_derived2()
obj.show_hybrid()
