from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo1(request):
    return HttpResponse("this is a cat")
def home(request):
    return HttpResponse('this is a home page')
def about(request):
    return render(request,'about.html')
def contact(request):
    return HttpResponse('this includes contact details')
def details(request):
    return render(request,'details.html')
def thankspage(request):
    return HttpResponse('this is a thanks page')
def addition(request):
    x=request.GET['A']
    y=request.GET['B']
    res=x+y
    return render(request,'result.html',{'result':res})