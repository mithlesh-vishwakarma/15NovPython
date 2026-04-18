'''
operator overloading in python: the operator overloading is not supported directly. it uses special methods to achieve operator overloading.
'''
class A:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def __add__(self,other):
    return self.a+other.a,self.b+other.b
  def __mul__(self,other):
    return self.a*other.a,self.b*other.b

a=A(1,2)
b=A(3,4)
print(a+b)
print(a*b)