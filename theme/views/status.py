from django.shortcuts import get_object_or_404,render,redirect
from ..models import StatusModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.status_form import StatusForm
#from ..models import Category

def viewStatus(request):
    context={}
    context["statuses"]=StatusModel.objects.all()
    return render(request, "flight_status/view.html",context)

def addStatus(request):
    context={}
    form=StatusForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewStatus")
    context['form']=form
    return render(request,"flight_status/add.html",context)

def updateStatus(request,id):
    context={}
    obj=get_object_or_404(StatusModel,id=id)
    form=StatusForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewStatus")
    context["form"]=form
    return render(request,"flight_status/edit.html",context)

def deleteStatus(request,id):
    context={}
    obj=get_object_or_404(StatusModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewStatus")
    return render(request,"flight_status/view.html",context)