'''
inheritance:
inheritance in python is an object-oriented programming concept where one class can inherit properties and methods from another class.
- the class whose properties and methods are inherited is called the parent class or superclass.
- the class that inherits the properties and methods is called the child class or subclass.
- the child class can access all the properties and methods of the parent class.
- the child class can also have its own properties and methods.
- the child class can override the properties and methods of the parent class.

types of inheritance:
1. single inheritance
2. multiple inheritance
3. multilevel inheritance
4. hierarchical inheritance
5. hybrid inheritance


1. single inheritance:
when a child class inherits properties and methods from a single parent class, it is called single inheritance.

class parent:
  def m1(self):
    print("parent class")

class child(parent):
  def m2(self):
    print("child class")

c=child()
c.m1()
c.m2()


2. multiple inheritance:
when a child class inherits properties and methods from multiple parent classes, it is called multiple inheritance.

class parent1:
  def m1(self):
    print("parent1 class")

class parent2:
  def m2(self):
    print("parent2 class")

class child(parent1,parent2):
  def m3(self):
    print("child class")

c=child()
c.m1()
c.m2()
c.m3()


3. multilevel inheritance:
when a child class inherits properties and methods from a parent class, and that parent class inherits properties and methods from another parent class, it is called multilevel inheritance.

class parent1:
  def m1(self):
    print("parent1 class")

class parent2(parent1):
  def m2(self):
    print("parent2 class")

class child(parent2):
  def m3(self):
    print("child class")

c=child()
c.m1()
c.m2()
c.m3()


4. hierarchical inheritance:
when multiple child classes inherit properties and methods from a single parent class, it is called hierarchical inheritance.

class parent:
  def m1(self):
    print("parent class")

class child1(parent):
  def m2(self):
    print("child1 class")

class child2(parent):
  def m3(self):
    print("child2 class")

c1=child1()
c2=child2()
c1.m1()
c1.m2()
c2.m1()
c2.m3()


5. hybrid inheritance:
when multiple child classes inherit properties and methods from multiple parent classes, and there is a combination of single, multiple, multilevel, and hierarchical inheritance, it is called hybrid inheritance.

class parent1:
  def m1(self):
    print("parent1 class")

class parent2:
  def m2(self):
    print("parent2 class")

class child1(parent1):
  def m3(self):
    print("child1 class")

class child2(parent1,parent2):
  def m4(self):
    print("child2 class")

c1=child1()
c2=child2()
c1.m1()
c1.m3()
c2.m1()
c2.m2()
c2.m4()

'''


class A:
  def __init__(self):
    print("class A constructor")
  def display(self):
    print("class A display calling")

class B:
  def __init__(self):
    print("class B constructor")
  def display(self):
    print("class B display calling")

class C(A,B):
  def __init__(self):
    print("C constructor")
    A.__init__(self)
    # A.display(self)
    B.display(self)

    # B.__init__(self)
    # super().__init__()
    # super().display()

c=C()
c.display()

