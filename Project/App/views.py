from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    return render(request,'Base.html')

def Productos(request):
    # ---> Guardamos todos los Productos en una variable
    Villalva=Producto.objects.all()
    data={
        # ---> Enviamos todos los productos a la palabra reservada
        'tabla':Villalva
    }
    # --------------->Enviamos mediante la Palabra Data
    return render(request,'Productos.html',data)
