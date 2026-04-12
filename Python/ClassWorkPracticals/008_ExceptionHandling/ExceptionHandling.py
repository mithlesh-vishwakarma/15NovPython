print("program started")

try:
    a = 10
    # b = a / 10
    b = a / 0
    # print(b)
    print(10 + "xyz")
except Exception as e:
    print("Exception Handled")
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

else:
    print("this is else part")

finally:
    print("always executable")
