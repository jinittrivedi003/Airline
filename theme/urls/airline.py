from django.urls import path
from ..views.airline import *
airlineURL=[
    path('viewAirline/',viewAirline,name="viewAirline"),
    path('addAirline/',addAirline,name="addAirline"),  
    path('updateAirline/<id>',updateAirline,name="updateAirline"), 
    path('deleteAirline/<id>',deleteAirline,name="deleteAirline"), 
]