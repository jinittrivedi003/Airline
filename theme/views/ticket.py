from django.shortcuts import get_object_or_404,render,redirect
from ..models import TicketModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.ticket_form import TicketForm
#from ..models import Category

def viewTicket(request):
    context={}
    context["tickets"]=TicketModel.objects.all()
    return render(request, "ticket/view.html",context)

def addTicket(request):
    context={}
    form=TicketForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewTicket")
    context['form']=form
    return render(request,"ticket/add.html",context)

def updateTicket(request,ticket_id):
    context={}
    obj=get_object_or_404(TicketModel,ticket_id=ticket_id)
    form=TicketForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewTicket")
    context["form"]=form
    return render(request,"ticket/edit.html",context)

def deleteTicket(request,ticket_id):
    context={}
    obj=get_object_or_404(TicketModel,ticket_id=ticket_id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewTicket")
    return render(request,"ticket/view.html",context)