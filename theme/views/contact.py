from django.shortcuts import get_object_or_404,render,redirect
from ..models import ContactModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.contact_form import ContactForm
#from ..models import Category

def viewContact(request):
    context={}
    context["contacts"]=ContactModel.objects.all()
    return render(request, "contact_us/view.html",context)

def addContact(request):
    context={}
    form=ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewContact")
    context['form']=form
    return render(request,"contact_us/add.html",context)

def updateContact(request,id):
    context={}
    obj=get_object_or_404(ContactModel,id=id)
    form=ContactForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewContact")
    context["form"]=form
    return render(request,"contact_us/edit.html",context)

def deleteContact(request,id):
    context={}
    obj=get_object_or_404(ContactModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewContact")
    return render(request,"contact_us/view.html",context)