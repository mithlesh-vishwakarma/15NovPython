class Salary:
    def __init__(self,salary,bonus):
        self.salary = salary
        self.bonus = bonus

    def annual_salary(self):
        return (self.salary*12)+self.bonus
    
class Employee:

    def __init__(self,name,age,salary,bonus):
        self.name = name
        self.age = age
        self.sal_obj= Salary(salary,bonus)
    
    def total_salary(self):
        return self.sal_obj.annual_salary()


e = Employee("Manish",25,10000,2000)
print(e.total_salary())






# ============================================
# PYTHON OOP - COMPOSITION NOTES
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

Salary class:
• salary → monthly salary
• bonus → extra amount

annual_salary() → calculates yearly salary
"""


# ============================================
# 2. EMPLOYEE CLASS (CREATES SALARY OBJECT)
# ============================================

class Employee:

    def __init__(self, name, age, salary, bonus):
        self.name = name
        self.age = age

        # Composition: object created inside class
        self.sal_obj = Salary(salary, bonus)

    def total_salary(self):
        return self.sal_obj.annual_salary()


"""
Explanation:

Employee creates Salary object inside itself.

This is Composition:
→ Strong relationship

Employee depends on Salary class
Salary object is created internally
"""


# ============================================
# 3. OBJECT CREATION
# ============================================

e = Employee("Manish", 25, 10000, 2000)

print(e.total_salary())   # Output: 122000


"""
Calculation:

salary = 10000 per month
annual = 10000 * 12 = 120000
bonus = 2000

Total = 122000
"""


# ============================================
# AGGREGATION vs COMPOSITION
# ============================================

# Aggregation:
# → Object passed from outside
# → Weak relationship
# → Independent objects

# Composition:
# → Object created inside class
# → Strong relationship
# → Dependent objects


# ============================================
# KEY POINTS
# ============================================

# • Composition → "Has-A" strong relationship
# • Employee HAS-A Salary (internally created)
# • Better encapsulation and control
# • Used in real-world system design


# ============================================
# REAL-WORLD EXAMPLE
# ============================================

# Car → Engine
# House → Rooms
# Company → Departments

# Used in:
# • ERP systems
# • Payroll systems
# • Backend architecture