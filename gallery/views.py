from django.shortcuts import render

from gallery.models import Image, Location

# Create your views here.

def index(request):
    title = 'JK Gallery'
    all_images = Image.objects.all()
    locations = Location.get_location()
    args = {
        "title":title,
        "all_images":all_images,
        "locations":locations
    }

    return render(request, 'index.html',args)

def image_location(request,location):
    images = Image.filter_by_location(location)
    args = {
         "images":images
    }
    
    return render(request, 'locations.html',args)

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"
        args = {
            "message":message,
            "images":searched_images
        }

        return render(request, 'search.html',args)

    else:
        message = "You haven't searched for any image category"
        return render(request,{"message":message})
    
