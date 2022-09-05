from distutils.text_file import TextFile
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    pass
class CategoryModel(models.Model):
    title=models.CharField(max_length=200)  
    description= models.TextField()

class AirlineModel(models.Model):
    id=models.CharField(max_length=8,unique=True,primary_key=True)
    From=models.TextField(max_length=15)
    To=models.TextField(max_length=15)
    Departing_Date=models.DateField()
    Returning_Date=models.DateField()
    Class=models.CharField(max_length=15)

class StatusModel(models.Model):
    Flightno=models.TextField(max_length=10)
    DepartureDate=models.DateField()
    Origin=models.TextField(max_length=20)
    Destination=models.TextField(max_length=20)

class CargoModel(models.Model):
    Origin=models.TextField(max_length=20)
    Destination=models.TextField(max_length=20)
    Date=models.DateField()
    Goods_Description=models.TextField()
    Weight=models.IntegerField()
    Product=models.TextField(max_length=30)

def __str__(self):
    return self.title

class Meta:
    db_table="dashboard_user"