import this
from django.shortcuts import render

# Create your views here.
listItem = []

def index(request):
    return render(request, "index.html")

def list(request):
    if request.method == 'POST': # If the form has been submitted...
        val = request.POST['newItem']
        listItem.append(val)
        
    return render(request, "list.html", {"listItem": listItem})