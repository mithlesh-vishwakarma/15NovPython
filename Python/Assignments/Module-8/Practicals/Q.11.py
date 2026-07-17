# Q.11 Write a Python program to create a class and access the properties of the class using an object. 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
