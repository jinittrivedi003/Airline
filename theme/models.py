from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    pass
class CategoryModel(models.Model):
    title=models.CharField(max_length=200)  #
    description= models.TextField()

def __str__(self):
    return self.title

class Meta:
    db_table="dashboard_user"