from socket import fromshare
from django import forms
from ..models import CarModel
from django.db import models

class CarForm(forms.ModelForm):
    
    class Meta:
        model=CarModel

        fields=[
            "Pickup",
            "Dropoff",
            "PickupDate",
            "PickupTime",
        ]