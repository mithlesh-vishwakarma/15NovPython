# Q.18 Write a Python program to demonstrate the use of super() in inheritance

class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name from Parent: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        super().show()
        print(f"Age from Child: {self.age}")

child = Child("Bob", 10)
child.show()
