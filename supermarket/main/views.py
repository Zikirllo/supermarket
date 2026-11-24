from django.shortcuts import render
from .models import *
# Create your views here.
def Homepage(request):
    p=Product.objects.all()
    con={
        "product":p
    }
    return render(request,"index.html",con)