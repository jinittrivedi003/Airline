from django.shortcuts import get_object_or_404,render,redirect
from ..models import FareModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.fare_form import FareForm
#from ..models import Category

def viewFare(request):
    context={}
    context["fares"]=FareModel.objects.all()
    return render(request, "fare/view.html",context)

def addFare(request):
    context={}
    form=FareForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewFare")
    context['form']=form
    return render(request,"fare/add.html",context)

def updateFare(request,id):
    context={}
    obj=get_object_or_404(FareModel,id=id)
    form=FareForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewFare")
    context["form"]=form
    return render(request,"fare/edit.html",context)

def deleteFare(request,id):
    context={}
    obj=get_object_or_404(FareModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewFare")
    return render(request,"fare/view.html",context)