from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'UserPage/home.html')


def page(request):
    return render(request,'UserPage/page.html')

def logout(request):
    return HttpResponse('hhh')