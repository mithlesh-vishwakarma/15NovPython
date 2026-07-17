# #aggregaton
# class Salary:
#     def __init__(self,salary,bonus):
#         self.salary = salary
#         self.bonus = bonus

#     def annual_salary(self):
#         return (self.salary*12)+self.bonus
    
# class Employee:

#     def __init__(self,name,age,sal_obj):
#         self.name = name
#         self.age = age
#         self.sal_obj= sal_obj
    
#     def total_salary(self):
#         return self.sal_obj.annual_salary()


# sal_obj = Salary(5000,2000)
# e = Employee("Yash",25,sal_obj)
# e1 = Employee("krish",23,sal_obj)
# print(e.total_salary())
# print(e1.total_salary())






# ============================================
# PYTHON OOP - AGGREGATION NOTES
# ============================================


# ============================================
# 1. SALARY CLASS
# ============================================

class Salary:

    def __init__(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus

    def annual_salary(self):
        return (self.salary * 12) + self.bonus


"""
Explanation:

Salary class handles salary-related data

salary → monthly salary
bonus → extra amount

annual_salary() → calculates yearly salary
"""


# ============================================
# 2. EMPLOYEE CLASS (USES SALARY OBJECT)
# ============================================

class Employee:

    def __init__(self, name, age, sal_obj):
        self.name = name
        self.age = age
        self.sal_obj = sal_obj   # Aggregation (object inside another class)

    def total_salary(self):
        return self.sal_obj.annual_salary()


"""
Explanation:

Employee class uses Salary class object

sal_obj → object of Salary class

This is called Aggregation:
→ One class uses another class object
"""


# ============================================
# 3. OBJECT CREATION
# ============================================

sal_obj = Salary(5000, 2000)

e = Employee("Yash", 25, sal_obj)
e1 = Employee("Krish", 23, sal_obj)

print(e.total_salary())
print(e1.total_salary())


"""
Explanation:

Same Salary object is shared between multiple employees

This shows:
• Loose coupling
• Reusability
"""


# ============================================
# KEY POINTS
# ============================================

# • Aggregation → "Has-A" relationship
#   Employee HAS-A Salary

# • Objects are independent
#   Salary object can exist without Employee

# • Used for code reusability and modular design


# ============================================
# AGGREGATION vs COMPOSITION
# ============================================

# Aggregation:
# → Weak relationship
# → Objects can exist independently

# Composition:
# → Strong relationship
# → Objects depend on each other


# ============================================
# REAL-WORLD EXAMPLE
# ============================================

# Employee → has Salary
# Student → has Address
# Car → has Engine

# Helps in building large systems like:
# • ERP
# • Payroll system
# • Management software