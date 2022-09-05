from django.shortcuts import get_object_or_404,render,redirect
from ..models import AirlineModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.airline_form import AirlineForm
#from ..models import Category

def viewAirline(request):
    context={}
    context["airlines"]=AirlineModel.objects.all()
    return render(request, "airline_book/view.html",context)

def addAirline(request):
    context={}
    form=AirlineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewAirline")
    context['form']=form
    return render(request,"airline_book/add.html",context)

def updateAirline(request,id):
    context={}
    obj=get_object_or_404(AirlineModel,id=id)
    form=AirlineForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewAirline")
    context["form"]=form
    return render(request,"airline_book/edit.html",context)

def deleteAirline(request,id):
    context={}
    obj=get_object_or_404(AirlineModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewAirline")
    return render(request,"airline_book/view.html",context)