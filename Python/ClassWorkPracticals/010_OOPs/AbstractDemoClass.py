from abc import ABC,abstractmethod

class Abs(ABC):

    @abstractmethod
    def display(self):
        pass

class AbsImpl(Abs):

    def display(self):
        print("display calling")

a = AbsImpl()
a.display()







# ============================================
# PYTHON OOP - ABSTRACTION (ABSTRACT CLASS)
# ============================================

from abc import ABC, abstractmethod   # import abstract base class tools


# ============================================
# 1. ABSTRACT CLASS
# ============================================

class Abs(ABC):   # Inherit from ABC to make abstract class

    @abstractmethod
    def display(self):
        pass   # abstract method (no implementation)


"""
Explanation:

• Abstract class → Cannot create object
• Used as blueprint for other classes
• Contains abstract methods (only declaration, no body)
"""


# ============================================
# 2. CHILD CLASS (IMPLEMENTATION)
# ============================================

class AbsImpl(Abs):

    def display(self):   # must implement abstract method
        print("display calling")


"""
Explanation:

• Child class must implement all abstract methods
• Otherwise it will throw error
"""


# ============================================
# 3. OBJECT CREATION
# ============================================

a = AbsImpl()   # object of child class
a.display()     # Output: display calling


"""
Explanation:

• Cannot create object of Abs class
• Must use child class
"""


# ============================================
# IMPORTANT POINTS
# ============================================

# ❌ Not allowed:
# a = Abs()   # Error → Can't instantiate abstract class

# ✔ Allowed:
# a = AbsImpl()


# ============================================
# WHY USE ABSTRACT CLASS?
# ============================================

# • Enforces method implementation in child classes
# • Provides common structure
# • Helps in large projects and clean architecture


# ============================================
# REAL-WORLD EXAMPLE
# ============================================

# Example: Payment System

# Abstract class:
# → defines method like pay()

# Child classes:
# → CreditCard → implement pay()
# → UPI → implement pay()
# → NetBanking → implement pay()


# ============================================
# KEY POINTS
# ============================================

# • ABC → Abstract Base Class
# • @abstractmethod → declare abstract method
# • Cannot create object of abstract class
# • Child class must implement all abstract methods