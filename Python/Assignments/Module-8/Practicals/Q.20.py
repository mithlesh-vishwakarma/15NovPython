# Q.20 Write a Python program to show method overriding.

class Animal:
    def sound(self):
        print("Generic animal sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

animal = Animal()
animal.sound()

cat = Cat()
cat.sound()
