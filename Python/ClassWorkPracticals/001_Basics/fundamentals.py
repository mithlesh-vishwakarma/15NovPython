# ============================================
# PYTHON PRINT FUNCTION & STRING HANDLING NOTES
# ============================================


# ============================================
# 1. BASIC PRINT STATEMENTS
# ============================================

print("Hello python")
print('Hello   world')

print("""Hello python
fffd
fdfdfd
fdf
""")


"""
Explanation:

print() → Used to display output on the screen.

Single quotes (' ') and double quotes (" ") both work for strings.

Triple quotes (''' ''' or """ """) allow multi-line strings.
"""


# ============================================
# 2. PRINT WITH MULTIPLE VALUES (sep parameter)
# ============================================

print("Python", "Java", "Php", "Android", sep=" -|- ")


"""
Explanation:

sep parameter → Defines separator between multiple values.

Default separator is space.
Here it is changed to:  -|- 
"""


# ============================================
# 3. PRINT WITH END PARAMETER
# ============================================

print("Hello", end=" - ")
print("python")


"""
Explanation:

end parameter → Controls what gets printed at the end.

Default is newline (\n).
Here it prints " - " instead of moving to next line.
"""


# ============================================
# 4. ESCAPE CHARACTERS
# ============================================

print('Hello " Python')
print("Hello\b \\\" C ")


"""
Explanation:

Escape characters start with backslash (\).

\"  → Print double quote
\\  → Print backslash
\b  → Backspace (removes previous character)

Used when special characters need to be printed.
"""


# ============================================
# 5. TAKING USER INPUT
# ============================================

a = input("Enter value of a : ")
print(a)


"""
Explanation:

input() → Takes user input as string by default.

Even if user enters number, it will be stored as string.
To convert:
int(a)
float(a)
"""


# ============================================
# 6. STRING FORMATTING
# ============================================

name = "abc"
email = "abc@gmail.com"

print("my name is {1} and email is {0}".format(name, email))
print(f"my name is {name} and email is {email}")


"""
Explanation:

Method 1 → format()
{0}, {1} represent position index.

Method 2 → f-string (recommended)
f"string {variable}"

F-strings are cleaner and modern way.
"""


# ============================================
# 7. RAW STRING
# ============================================

print(r"Hello\b \\\" C ")


"""
Explanation:

r before string → Raw string.

Raw string ignores escape characters.
Everything prints exactly as written.
"""


# ============================================
# 8. STRING SPLIT METHOD
# ============================================

print("sun rises in east".split("s"))


"""
Explanation:

split() → Breaks string into list based on separator.

Example:
"sun rises in east".split("s")

It splits wherever "s" appears.
Output will be a list.
"""