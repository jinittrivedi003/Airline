from django.shortcuts import get_object_or_404,render,redirect
from ..models import CarModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.car_form import CarForm
#from ..models import Category

def viewCar(request):
    context={}
    context["cars"]=CarModel.objects.all()
    return render(request, "car_book/view.html",context)

def addCar(request):
    context={}
    form=CarForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewCar")
    context['form']=form
    return render(request,"car_book/add.html",context)

def updateCar(request,id):
    context={}
    obj=get_object_or_404(CarModel,id=id)
    form=CarForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewCar")
    context["form"]=form
    return render(request,"car_book/edit.html",context)

def deleteCar(request,id):
    context={}
    obj=get_object_or_404(CarModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewCar")
    return render(request,"car_book/view.html",context)