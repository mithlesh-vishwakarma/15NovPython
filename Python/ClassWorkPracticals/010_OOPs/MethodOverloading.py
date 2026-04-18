'''
Method Overloading:
Method overloading is a concept in object-oriented programming where multiple methods in a class have the same name but different parameters.
but in python this is not supported directly.
it uses default arguments to achieve method overloading. standard module from library is multipledispatch. @dispatch decorator is used to achieve method overloading.

class A:
  def add(self,a,b):
    print(a+b)
  def add(self,a,b,c):
    print(a+b+c)

a=A()
a.add(1,2)
a.add(1,2,3)


Method Overriding:
Method overriding is a concept in object-oriented programming where a child class provides its own implementation of a method that is already defined in its parent class.

class A:
  def add(self,a,b):
    print(a+b)

class B(A):
  def add(self,a,b,c):
    print(a+b+c)

a=A()
a.add(1,2)
b=B()
b.add(1,2,3)

'''

from multipledispatch import dispatch

class A:
  @dispatch(int,int)
  def add(self,a,b):
    print(a+b)
  @dispatch(int,int,int)
  def add(self,a,b,c):
    print(a+b+c)

a=A()
a.add(1,2)
a.add(1,2,3)
