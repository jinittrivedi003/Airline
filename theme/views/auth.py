from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from ..forms.register import CustomUserCreationForm

def index(request):
    return render(request,"index.html")

def LogIn(request):
    return render(request,"sidebar.html")

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'