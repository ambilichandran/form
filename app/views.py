from django.shortcuts import render
from .models import Student

def index(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        std=Student(name=name,age=age)
        std.save()
    return render(request,"index.html")
