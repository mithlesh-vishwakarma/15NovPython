marks=int(input("Enter your marks: "))
if marks>=91 and marks<=100:
  print("Grade A")
elif marks>=71 and marks<=90:
  print("Grade B")
elif marks>=51 and marks<=70:
  print("Grade C")
elif marks>=35 and marks<=50:
  print("Grade D")
elif marks>=0 and marks<=34:
  print("Grade E")
else:
  print("Invalid marks please choose correct marks")
