from django.shortcuts import get_object_or_404,render,redirect
from ..models import CargoModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.cargo_form import CargoForm
#from ..models import Category

def viewCargo(request):
    context={}
    context["cargoes"]=CargoModel.objects.all()
    return render(request, "cargo/view.html",context)

def addCargo(request):
    context={}
    form=CargoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewCargo")
    context['form']=form
    return render(request,"cargo/add.html",context)

def updateCargo(request,id):
    context={}
    obj=get_object_or_404(CargoModel,id=id)
    form=CargoForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewCargo")
    context["form"]=form
    return render(request,"cargo/edit.html",context)

def deleteCargo(request,id):
    context={}
    obj=get_object_or_404(CargoModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewCargo")
    return render(request,"cargo/view.html",context)