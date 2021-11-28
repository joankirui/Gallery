from django.shortcuts import render

from gallery.models import Image, Location

# Create your views here.

def index(request):
    title = 'JK Gallery'
    all_images = Image.objects.all()
    locations = Location.get_location()

    return render(request, 'index.html', {"title":title,"all_images":all_images,"locations":locations})

def image_location(request,location):
    images = Image.filter_by_location(location)
    
    return render(request, 'locations.html', {"images":images})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for any image category"
        return render(request,{"message":message})
    
