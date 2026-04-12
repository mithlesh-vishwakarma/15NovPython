def NumbersOnly():
  def check(value):
    if str(value).isdigit():
      return value
    else:
      print("Please enter a valid number")
  return check

def StringOnly():
  def check(value):
    if str(value).isalpha():
      return value
    else:
      print("Please enter a valid string")
  return check


@NumbersOnly()
def get(value):
  print(value)

get(10)


