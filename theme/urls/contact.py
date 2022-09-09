from django.urls import path
from ..views.contact import *
contactURL=[
    path('viewContact/',viewContact,name="viewContact"),
    path('addContact/',addContact,name="addContact"),  
    path('updateContact/<id>',updateContact,name="updateContact"), 
    path('deleteContact/<id>',deleteContact,name="deleteContact"), 
]