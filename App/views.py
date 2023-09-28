from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Index(request):
    print("ssssssssssssssssssss")
    # return HttpResponse('Gaurvish')
    return render(request, "index.html")

def About(request):
    print("ssssssssssssssssssss")
    # return HttpResponse('Gaurvish')
    return render(request, "about.html")

def Contact(request):
    print("ssssssssssssssssssss")
    # return HttpResponse('Gaurvish')
    return render(request, "contact.html")

def Services(request):
    print("ssssssssssssssssssss")
    # return HttpResponse('Gaurvish')
    return render(request, "services.html")

def Doctor(request):
    print("ssssssssssssssssssss")
    # return HttpResponse('Gaurvish')
    return render(request, "doctor.html")

def Blog(request):
    return render(request, "blog.html")