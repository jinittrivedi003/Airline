from django.shortcuts import get_object_or_404,render,redirect
from ..models import PassengerModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.passenger_form import PassengerForm
#from ..models import Category

def viewPassenger(request):
    context={}
    context["passengers"]=PassengerModel.objects.all()
    return render(request, "passenger/view.html",context)

def addPassenger(request):
    context={}
    form=PassengerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewPassenger")
    context['form']=form
    return render(request,"passenger/add.html",context)

def updatePassenger(request,Reg_id):
    context={}
    obj=get_object_or_404(PassengerModel,Reg_id=Reg_id)
    form=PassengerForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewPassenger")
    context["form"]=form
    return render(request,"passenger/edit.html",context)

def deletePassenger(request,Reg_id):
    context={}
    obj=get_object_or_404(PassengerModel,Reg_id=Reg_id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewPassenger")
    return render(request,"passenger/view.html",context)