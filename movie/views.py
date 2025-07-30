from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie
# Create your views here.


def home(request):
    # return render(request, 'home.html')
    #return HttpResponse('<h1>Welcome to home page</h1>')
    # return render(request, 'home.html', {'name': 'Athina Cappelletti'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchMovie': searchTerm, 'movies': movies})

def about(request):
    return render(request, 'about.html')
