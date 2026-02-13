from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import *

def index(request:HttpRequest):

    product=Product.objects.all()


    context={
        "title":"Asu Market",
        "products":product
    }
    return render(request,"app/index.html",context)

def about(request:HttpRequest):
    return HttpResponse('<h3 style="color:blue;">Bu sayt asosan marketlarni savdosini yaxshilash uchun</h3>')







