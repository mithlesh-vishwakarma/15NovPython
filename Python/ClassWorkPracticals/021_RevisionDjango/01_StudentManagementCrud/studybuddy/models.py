from django.db import models

class Course(models.Model):
  name=models.CharField(max_length=30)
  duration=models.CharField(max_length=50)
  fees=models.DecimalField(max_digits=10,decimal_places=2)

  def __str__(self):
      return self.name


class Subject(models.Model):
  name=models.CharField(max_length=20)
  course=models.ManyToManyField(Course)

  def __str__(self):
    return self.name

class Student(models.Model):
  profile=models.ImageField(upload_to="image",null=True)
  student_id=models.CharField(max_length=12)
  first_name=models.CharField(max_length=20)
  last_name=models.CharField(max_length=20)
  date_of_birth=models.DateField()
  email=models.EmailField()
  phone=models.CharField(max_length=10)
  course=models.ForeignKey(Course,on_delete=models.CASCADE)
  admission_date=models.DateField()