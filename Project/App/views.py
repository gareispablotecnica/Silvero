from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'Base.html')

def Productos(request):
    return render(request,'Productos.html')