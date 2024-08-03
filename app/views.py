from django.shortcuts import render

# Create your views here.


def home(request):
    
    return render(request, "home.html")

def timeline(request):
    return render(request, "timeline.html")