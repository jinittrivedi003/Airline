from django.shortcuts import get_object_or_404,render,redirect
from ..models import BranchModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.branch_form import BranchForm
#from ..models import Category

def viewBranch(request):
    context={}
    context["branches"]=BranchModel.objects.all()
    return render(request, "branch/view.html",context)

def addBranch(request):
    context={}
    form=BranchForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewBranch")
    context['form']=form
    return render(request,"branch/add.html",context)

def updateBranch(request,branch_code):
    context={}
    obj=get_object_or_404(BranchModel,branch_code=branch_code)
    form=BranchForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewBranch")
    context["form"]=form
    return render(request,"branch/edit.html",context)

def deleteBranch(request,branch_code):
    context={}
    obj=get_object_or_404(BranchModel,branch_code=branch_code)
    if request.method=="GET":
        obj.delete()
        return redirect("viewBranch")
    return render(request,"branch/view.html",context)