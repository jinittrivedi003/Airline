from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns=[
     path('home/',views.home,name='home'),
     path('Book/',views.book,name="book"),
     path('offer/',views.offer,name="offer"),
     path('services/',views.services,name="services"),
     path('safety/',views.safety,name="safety"),
     path('contacts/',views.contacts,name="contacts"),
     path('contactuser/',views.contactuser,name="contactuser"),
     path('airline/',views.airline,name="airline"),
     path('branch/',views.branch,name="branch"),
]