from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def home(request):
    return render(request, 'home.html')
    
def Register(request):
    Name = request.GET['Name']
    PassWord = request.GET['PassWord']
    Address = request.GET['Address']
    Mail = request.GET['Mail']
    return render(request, "result.html", {'Name':Name,'PassWord':PassWord,'Address':Address,'Mail':Mail})

    