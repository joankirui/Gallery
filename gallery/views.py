from django.shortcuts import render

from gallery.models import Image, Location

# Create your views here.

def index(request):
    title = 'JK Gallery'
    all_images = Image.objects.all()
    locations = Location.get_location()

    return render(request, 'index.html', {"title":title,"all_images":all_images,"locations":locations})
    
