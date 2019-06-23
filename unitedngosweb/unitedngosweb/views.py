# user file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html",{"creatorName":"shantanu sharma"})

def seeanswer(request):
    text=request.POST.get("test","no text found")
    return HttpResponse("lay loo samaan : "+str(text))