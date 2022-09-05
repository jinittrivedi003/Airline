from django.urls import path
from ..views.cargo import *
cargoURL=[
    path('viewCargo/',viewCargo,name="viewCargo"),
    path('addCargo/',addCargo,name="addCargo"),  
    path('updateCargo/<id>',updateCargo,name="updateCargo"), 
    path('deleteCargo/<id>',deleteCargo,name="deleteCargo"), 
]