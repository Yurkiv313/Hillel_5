from django.db import models


# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_data = models.DateField()
    subject = models.CharField(max_length=50)
