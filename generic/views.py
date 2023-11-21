from django.shortcuts import render

# Create your views here.

def genericpage1(request):
    return render(request,'genericpage1.html')

def genericpage2(request):
    return render(request,'genericpage2.html')