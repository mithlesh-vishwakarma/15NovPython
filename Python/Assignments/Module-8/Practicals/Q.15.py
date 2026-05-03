# Q.15 Write a Python program to show multiple inheritance. 

class Father:
    def father_trait(self):
        print("Father's trait")

class Mother:
    def mother_trait(self):
        print("Mother's trait")

class Child(Father, Mother):
    def child_trait(self):
        print("Child's trait")

child = Child()
child.father_trait()
child.mother_trait()
child.child_trait()
