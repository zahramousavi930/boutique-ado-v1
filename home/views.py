from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
from django.shortcuts import render

def profile_view(request):
    # Your view logic here
    return render(request, 'profile.html')
