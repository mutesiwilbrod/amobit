from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'oursite/index.html',{})

def contact(request):
    return render(request,'oursite/contact-us.html', {})


def register(request):
    return render(request,'oursite/register.html',{})