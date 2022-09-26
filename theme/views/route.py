from django.shortcuts import get_object_or_404,render,redirect
from ..models import RouteModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.route_form import RouteForm
#from ..models import Category

def viewRoute(request):
    context={}
    context["routes"]=RouteModel.objects.all()
    return render(request, "route/view.html",context)

def addRoute(request):
    context={}
    form=RouteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewRoute")
    context['form']=form
    return render(request,"route/add.html",context)

def updateRoute(request,id):
    context={}
    obj=get_object_or_404(RouteModel,id=id)
    form=RouteForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewRoute")
    context["form"]=form
    return render(request,"route/edit.html",context)

def deleteRoute(request,id):
    context={}
    obj=get_object_or_404(RouteModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewRoute")
    return render(request,"route/view.html",context)