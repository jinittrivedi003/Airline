from django.shortcuts import render
from theme.models import *
from usersite.form.contactuser_form import contactuserForm
from django.contrib import messages
from usersite.models import *
# Create your views here.
def home(request):
    return render(request,"index.html")

def book(request):
     return render(request,"book.html")

def offer(request):
     return render(request,"offers.html")

def services(request):
     return render(request,"services.html")

def safety(request):
     return render(request,"safety.html")

def contacts(request):
      return render(request,"contacts.html")

def contactuser(request):
    if request.method == "POST":
        form = contactuserForm(request.POST or None)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"DONE BKA ,DATA SAVE :)")
                return render(request,'contacts.html')
            except:
                pass
    else:
        form = contactuserForm()
    return render(request,'contacts.html',{'form':form})

def airline(request):
    context={}
    context["airlines"]=AirlineModel.objects.all()
    return render(request,'airline/airlineview.html',context)

def branch(request):
    context={}
    context["branches"]=BranchModel.objects.all()
    return render(request,'branch/branchview.html',context)