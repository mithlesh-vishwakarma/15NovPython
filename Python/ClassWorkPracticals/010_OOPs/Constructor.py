
class Student:
  def __init__(self,id,name,email):
    self.id=id
    self.name=name
    self.email=email

  def display(self):
    print(self.id,self.name,self.email)

s=Student(10,"krish","krish@gmail.com")
s.display()
s1=Student(11,"amir","amir@gmail.com")
s1.display()
    
# ---------------------------------------------------------------



class Product:
  def __init__(self,id,name,price,qty):
    self.id=id
    self.name=name
    self.price=price
    self.qty=qty

  def display(self):
    print(self.id,self.name,self.price,self.qty)

s=Product(1,"Product1",100,5)
s.display()
s1=Product(2,"Product2",200,10)
s1.display()