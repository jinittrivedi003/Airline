from distutils.text_file import TextFile
from django.db import models
from django.contrib.auth.models import AbstractUser
 #Create your models here.

class UserModel(AbstractUser):
    userProfile=models.ImageField(upload_to="userProfile")
class CategoryModel(models.Model):
    title=models.CharField(max_length=200)  
    description= models.TextField()

class AirlineModel(models.Model):
    id=models.CharField(max_length=8,unique=True,primary_key=True)
    From=models.CharField(max_length=15,null=False,blank=False)
    To=models.CharField(max_length=15,null=False,blank=False)
    Departing_Date=models.DateField()
    Returning_Date=models.DateField()
    Class=models.CharField(max_length=15,null=False,blank=False)

class StatusModel(models.Model):
    Flightno=models.CharField(max_length=10,null=False,blank=False)
    DepartureDate=models.DateField()
    Origin=models.CharField(max_length=20)
    Destination=models.CharField(max_length=20)

class CargoModel(models.Model):
    Origin=models.CharField(max_length=20)
    Destination=models.CharField(max_length=100)
    Date=models.DateField()
    Goods_Description=models.TextField(null=False,blank=False)
    Weight=models.IntegerField(null=False,blank=False)
    Product=models.CharField(max_length=30)

class BookingModel(models.Model):
    Booking_id=models.CharField(max_length=8,null=False,blank=False)
    Firstname=models.CharField(max_length=25)
    Lastname=models.CharField(max_length=10)
    Mobile_number=models.CharField(max_length=12,null=False,blank=False)

class CarModel(models.Model):
    Pickup=models.CharField(max_length=20,null=False,blank=False)
    Dropoff=models.CharField(max_length=20)
    PickupDate=models.DateField()
    PickupTime=models.TimeField()
    
def __str__(self):
    return self.title

class Meta:
    db_table="dashboard_user"