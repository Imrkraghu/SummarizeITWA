from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Welcome, to SummarizeIT")
    return render(request, "home/index.html")

# home/views.py
def projects(request):
    return render(request, 'home/projects.html')

def about(request):
    return render(request, "home/about.html")

def team(request):
    return render(request, "home/team.html")

def contact(request):
    return render(request, "home/contact.html")

def rohit(request):
    return HttpResponse("hello Sir, my master you are the almighty")

def greet(request, name):
    return render(request, "home/greet.html", {
        "name": name.capitalize()
    })
