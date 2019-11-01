from django.shortcuts import render
from .models import Neighborhood,Business,Post,Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    hoods = Neighborhood.all_neighborhoods()
    # image_comments = Image.get_images()
    return render(request, 'home.html', {"hoods":hoods})

def hoods(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    businesses = Business.objects.filter(hood=hood)
    posts = Post.objects.filter(hood=hood)
    # image_comments = Image.get_images()
    return render(request, 'hoods.html', {"businesses":businesses,"hood":hood,"posts":posts})

def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_names = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_names})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})