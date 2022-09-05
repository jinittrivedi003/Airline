from django.urls import path
from ..views.car import *
carURL=[
    path('viewCar/',viewCar,name="viewCar"),
    path('addCar/',addCar,name="addCar"),  
    path('updateCar/<id>',updateCar,name="updateCar"), 
    path('deleteCar/<id>',deleteCar,name="deleteCar"), 
]