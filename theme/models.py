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

class BookingModel(models.Model):
    Booking_id=models.TextField(max_length=8)
    Firstname=models.TextField(max_length=25)
    Lastname=models.TextField(max_length=10)
    Mobile_number=models.CharField(max_length=12)

class CarModel(models.Model):
    Pickup=models.TextField(max_length=20)
    Dropoff=models.TextField(max_length=20)
    PickupDate=models.DateField()
    PickupTime=models.TimeField()

class ContactModel(models.Model):
    User_Name=models.TextField(max_length=20)
    Email=models.TextField(max_length=50)
    Subject=models.TextField(max_length=20)
    Message=models.TextField(max_length=100)

class FeedbackModel(models.Model):
    Quality_Score=models.TextField(max_length=10)
    Message=models.TextField(max_length=100)


    
def __str__(self):
    return self.title

class Meta:
    db_table="dashboard_user"