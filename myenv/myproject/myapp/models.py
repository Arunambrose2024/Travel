from django.db import models

# Create your models here.

class book(models.Model):
    Bname=models.CharField(max_length=250)
    Bemail=models.CharField(max_length=250)
    Bmob=models.CharField(max_length=250)
    Bdate=models.DateField
    Btime=models.TimeField
    guests=models.CharField(max_length=250)
    def __str__(self):
        return self.Bname

class signup(models.Model):
    name=models.CharField(max_length=250)
    Email=models.CharField(max_length=250)
    Username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.name