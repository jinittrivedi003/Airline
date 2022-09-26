from django.urls import path
from ..views.route import *
routeURL=[
    path('viewRoute/',viewRoute,name="viewRoute"),
    path('addRoute/',addRoute,name="addRoute"),  
    path('updateRoute/<id>',updateRoute,name="updateRoute"), 
    path('deleteRoute/<id>',deleteRoute,name="deleteRoute"), 
]