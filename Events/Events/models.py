from django.db import models

# Create your models here.


class Details(models.Model):
    name = models.CharField(max_length=30,unique=True)
    date = models.DateField()
    info = models.CharField(max_length=30)
    place = models.CharField(max_length=30)

class Cities(models.Model):
    city=models.CharField(max_length=30)

