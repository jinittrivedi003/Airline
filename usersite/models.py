from django.db import models

# Create your models here.
class contactuserModel(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Message=models.CharField(max_length=200)

