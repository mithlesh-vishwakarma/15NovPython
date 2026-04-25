from abc import ABC,abstractmethod

class Account(ABC):
    balance = 0
    def get_balance(self):
        print(f"Current balance is : {self.balance}")

    @abstractmethod
    def deposite(self,amount):
        pass
        
    @abstractmethod
    def withdrow(self, amount):
        pass


class Saving(Account):

    def deposite(self, amount):
        self.balance+=amount

    def withdrow(self, amount):
        if amount>self.balance:
            print("Insuffcient amount")
        else:
            self.balance-=amount

class Loan(Account):

    def withdrow(self, amount):
        self.balance+=amount
    
    def deposite(self, amount):
        if amount>self.balance:
            k = amount-self.balance
            print(f"apne jayad adiye : {k}")
            self.balance=0
        else:
            self.balance-=amount


# s = Saving()
# s.get_balance()
# s.deposite(8000)
# s.get_balance()
# s.withdrow(5000)
# s.get_balance()

l = Loan()
l.withdrow(15000)
l.deposite(115000)
l.get_balance()




# ============================================
# PYTHON OOP - BANK SYSTEM (ABSTRACTION + INHERITANCE)
# ============================================

from abc import ABC, abstractmethod


# ============================================
# 1. ABSTRACT CLASS (BASE CLASS)
# ============================================

class Account(ABC):

    balance = 0   # common variable

    def get_balance(self):
        print(f"Current balance is : {self.balance}")


    @abstractmethod
    def deposite(self, amount):
        pass

    @abstractmethod
    def withdrow(self, amount):
        pass


"""
Explanation:

Account → Abstract class (cannot create object)

Defines:
• common variable → balance
• common method → get_balance()
• abstract methods → deposite(), withdrow()

Child classes must implement abstract methods
"""


# ============================================
# 2. SAVING ACCOUNT CLASS
# ============================================

class Saving(Account):

    def deposite(self, amount):
        self.balance += amount   # add money

    def withdrow(self, amount):
        if amount > self.balance:
            print("Insufficient amount")
        else:
            self.balance -= amount


"""
Explanation:

Saving account:
• deposit → adds money
• withdraw → deducts money (with balance check)
"""


# ============================================
# 3. LOAN ACCOUNT CLASS
# ============================================

class Loan(Account):

    def withdrow(self, amount):
        self.balance += amount   # taking loan (increasing liability)

    def deposite(self, amount):
        if amount > self.balance:
            k = amount - self.balance
            print(f"Extra amount paid : {k}")
            self.balance = 0
        else:
            self.balance -= amount


"""
Explanation:

Loan account:
• withdraw → means taking loan (balance increases)
• deposit → means paying loan

If extra amount paid → balance becomes 0
"""


# ============================================
# 4. TESTING SAVING ACCOUNT
# ============================================

# s = Saving()
# s.get_balance()      # 0
# s.deposite(8000)    # add money
# s.get_balance()     # 8000
# s.withdrow(5000)    # withdraw
# s.get_balance()     # 3000


# ============================================
# 5. TESTING LOAN ACCOUNT
# ============================================

l = Loan()

l.withdrow(15000)   # taking loan
l.deposite(115000)  # paying loan

l.get_balance()     # Output: 0


# ============================================
# KEY CONCEPTS USED
# ============================================

# 1. Abstraction:
# → Account class defines structure

# 2. Inheritance:
# → Saving and Loan inherit Account

# 3. Polymorphism:
# → Same method names (deposit, withdraw)
#   but different behavior in each class


# ============================================
# IMPORTANT NOTES
# ============================================

# • Abstract class ensures all accounts follow same structure
# • Child classes implement their own logic
# • Code is reusable and scalable


# ============================================
# REAL-WORLD USE CASE
# ============================================

# Banking systems:
# • Saving Account
# • Loan Account
# • Current Account

# Each has different behavior but same interface