from django.db import models

# Create your models here.

class Register(models.Model):
  emp_id=models.IntegerField()
  emp_name=models.CharField(max_length=60)
  emp_age=models.IntegerField()
  username=models.CharField(max_length=50)
  image=models.FileField()
  def __str__(self):
    return self.emp_name
class login(models.Model):
  username=models.CharField(max_length=50)
  password=models.CharField(max_length=50)
