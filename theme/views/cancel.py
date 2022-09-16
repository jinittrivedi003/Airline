from pyexpat.errors import messages
from django.shortcuts import get_object_or_404,render,redirect
from ..models import CancellationModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.cancellation_form import CancellationForm
#from ..models import Category

def viewCancel(request):
    context={}
    context["cancels"]=CancellationModel.objects.all()
    return render(request, "cancel/view.html",context)

def addCancel(request):
    context={}
    form=CancellationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewCancel")
    context['form']=form
    return render(request,"cancel/add.html",context)

def updateCancel(request,Cancel_id):
    context={}
    obj=get_object_or_404(CancellationModel,Cancel_id=Cancel_id)
    form=CancellationForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewCancel")
    context["form"]=form
    return render(request,"cancel/edit.html",context)

def deleteCancel(request,Cancel_id):
    context={}
    obj=get_object_or_404(CancellationModel,Cancel_id=Cancel_id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewCancel")
    return render(request,"cancel/view.html",context)