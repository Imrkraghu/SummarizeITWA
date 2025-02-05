from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# showcase/views.py
from django.shortcuts import render
def SummarizeIT(request):
    return render(request, 'SummarizeIT/summarizeIT.html')
# home/views.py
def projects(request):
    return render(request, 'SummarizeIT/projects.html')

def about(request):
    return render(request, "SummarizeIT/about.html")

def team(request):
    return render(request, "SummarizeIT/team.html")

def contact(request):
    return render(request, "SummarizeIT/contact.html")

def rohit(request):
    return HttpResponse("hello Sir, my master you are the almighty")

