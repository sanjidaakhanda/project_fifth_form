from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    roll = models.IntegerField(primary_key= True)

