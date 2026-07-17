# Q.14 Write a Python program to show multilevel inheritance.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

puppy = Puppy()
puppy.speak()
puppy.bark()
puppy.weep()
