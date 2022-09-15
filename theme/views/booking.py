from pyexpat.errors import messages
from django.shortcuts import get_object_or_404,render,redirect
from ..models import BookingModel
from django.shortcuts import render
#from ..models import Category as CategoryForm
from ..forms.booking_form import BookingForm
#from ..models import Category

def viewBooking(request):
    context={}
    context["bookings"]=BookingModel.objects.all()
    return render(request, "booking/view.html",context)

def addBooking(request):
    context={}
    form=BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect( "viewBooking")
    context['form']=form
    return render(request,"booking/add.html",context)

def updateBooking(request,id):
    context={}
    obj=get_object_or_404(BookingModel,id=id)
    form=BookingForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("viewBooking")
    context["form"]=form
    return render(request,"booking/edit.html",context)

def deleteBooking(request,id):
    context={}
    obj=get_object_or_404(BookingModel,id=id)
    if request.method=="GET":
        obj.delete()
        return redirect("viewBooking")
    return render(request,"booking/view.html",context)