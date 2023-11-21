from django.shortcuts import render

# Create your views here.

def specificpage1(request):
    return render(request,'specificpage1.html')

def specificpage2(request):
    return render(request,'specificpage2.html')