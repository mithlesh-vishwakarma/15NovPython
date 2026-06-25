from django.db import models

# Create your models here.
# | Field           | Type            |
# | --------------- | --------------- |
# | id              | AutoField       |
# | student_id      | CharField       |
# | first_name      | CharField       |
# | last_name       | CharField       |
# | gender          | ChoiceField     |
# | date_of_birth   | DateField       |
# | email           | EmailField      |
# | phone           | CharField       |
# | address         | TextField       |
# | city            | CharField       |
# | state           | CharField       |
# | course          | ForeignKey      |
# | admission_date  | DateField       |
# | profile_picture | ImageField      |
# | status          | Active/Inactive |
class Course(models.Model):
  name=models.CharField(max_length=30)
  duration=models.models.CharField(max_length=50)
  fees=models.DecimalField(max_digits=10,decimal_places=2)

class Student(models.Model):
  id=models.AutoField()
  student_id=models.CharField(max_length=12)
  first_name=models.CharField(max_length=20)
  last_name=models.CharField(max_length=20)
  gender=models.ChoiceField()
  date_of_birth=models.DateField()
  email=models.EmailField()
  phone=models.CharField(max_length=10)
  address=models.TextField()
  city=models.CharField(max_length=20)
  state=models.CharField(max_length=20)
  course=models.ForeignKey()