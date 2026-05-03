# Q.12 Write a Python program to demonstrate the use of local and global variables in a class.

global_var = "I am global"

class MyClass:
    def __init__(self):
        self.class_var = "I am a class variable"

    def show_variables(self):
        local_var = "I am local to this method"
        print("Global Variable:", global_var)
        print("Class Variable:", self.class_var)
        print("Local Variable:", local_var)

obj = MyClass()
obj.show_variables()
