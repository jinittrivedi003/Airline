from socket import fromshare
from django import forms
from ..models import ContactModel
from django.db import models

class ContactForm(forms.ModelForm):
    
    class Meta:
        model=ContactModel

        fields=[
            "User_Name",
            "Email",
            "Subject",
            "Message",
        ]