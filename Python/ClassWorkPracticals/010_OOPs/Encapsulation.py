'''
Encapsulation:
Encapsulation is the process of wrapping data and methods that operate on the data in a single unit called a class.it is used to hide the internal implementation details of a class from the outside world.
- Encapsulation in python refers to the concept of restricting direct access to some of an object's components and exposing only the necessary features to the outside world.
- this concept is achieved by using access modifiers.
- this concept is also called as data hiding.

'''
class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display(self):
        print(self.__name,self.__age)

s=Student("mithlesh",21)
s.display()
# ----------------------------------------------------------

# ============================================
# PYTHON OOP - ENCAPSULATION NOTES
# ============================================


class Test:

    a = 10     # Public variable
    _b = 20    # Protected variable (by convention)
    __c = 30   # Private variable (name mangling)


    # ============================================
    # SET METHOD (MODIFY VALUES)
    # ============================================

    def set(self, a, b, c):
        self.a = a        # public
        self._b = b       # protected
        self.__c = c      # private


    # ============================================
    # GET METHODS (ACCESS VALUES)
    # ============================================

    def get_a(self):
        return self.a

    def get_b(self):
        return self._b

    def get_c(self):
        return self.__c


    # ============================================
    # DISPLAY METHOD
    # ============================================

    def display(self):
        print(self.a)      # public
        print(self._b)     # protected
        print(self.__c)    # private (accessible inside class)


# ============================================
# OBJECT CREATION
# ============================================

t = Test()

t.set(10, 20, 30)   # setting values

t.display()         # accessing inside class


# ============================================
# ACCESS USING GETTERS
# ============================================

print(t.get_a())   # public → accessible
print(t.get_b())   # protected → accessible (but not recommended outside)
print(t.get_c())   # private → accessible via method


# ============================================
# ACCESS LEVELS EXPLANATION
# ============================================

# 1. PUBLIC (a)
# → Can be accessed from anywhere
# Example: t.a


# 2. PROTECTED (_b)
# → Should not be accessed outside class (by convention)
# → Still accessible: t._b


# 3. PRIVATE (__c)
# → Cannot be accessed directly outside class
# → Python uses name mangling internally:
#    _ClassName__variable


# Example (not recommended):
# print(t._Test__c)


# ============================================
# KEY POINTS
# ============================================

# • Encapsulation → Binding data + methods together
# • Public → no restriction
# • Protected → convention-based restriction
# • Private → restricted using name mangling
# • Use getter/setter methods for controlled access
# ----------------------------------------------------------

# class test:
#     def __init__(self):
#         self.a=10
#         self._b=20
#         self.__c=30

#     def display(self):
#         print(self.a)
#         print(self._b)
#         print(self.__c)

# t=test()
# t.display()

# print(t.a)
# print(t._b)
# print(t.__c)


