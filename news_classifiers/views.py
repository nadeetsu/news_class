from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index.html", {})

def content(request):
     return render(request, "content.html", {'title': 'Content'})

def about(request):
     return render(request, "about.html", {'title': 'About'})

def trend(request):
     return render(request, "trend.html", {'title': 'Trend'})