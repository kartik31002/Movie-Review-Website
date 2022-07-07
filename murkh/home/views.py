import json
from django.shortcuts import render, HttpResponse
import requests
from . models import user, movies
from django.contrib import messages

apiBaseURL = 'https://api.themoviedb.org/3/'
apiKey = '3d9b4ef8cf0ea93474001f18dabe2e00'

imageBaseUrl = 'https://image.tmdb.org/t/p/'



# Create your views here.
def index(request):
    response = requests.get(apiBaseURL + 'movie/now_playing?api_key=' + apiKey).json()
    popular_movies = response["results"]
    movie_id = []
    for i in popular_movies:
        movie_id.append(i["id"])
    response3 = {}
    for i in movie_id:
        response3[i] = requests.get(apiBaseURL + 'movie/' + str(i) + '?api_key=' + apiKey).json()
    return render(request, 'index.html', {'response3' : response3})



def signup(request):
    return render(request, 'signup.html')



def registered(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if user.objects.filter(email__contains=email): 
            messages.error(request, 'Email already Exists!')
            return render(request, 'signup.html')
        else:
            User = user(username=username, email=email, password=password)
            User.save()
            return render(request, 'registered.html')


def searchresults(request):
    searchTerm = request.POST.get("searchTerm")
    response = requests.get(apiBaseURL + 'search/movie?api_key=' + apiKey + '&language=en-US&page=1&include_adult=false&query=' + searchTerm).json()
    popular_movies = response["results"]
    movie_id = []
    for i in popular_movies:
        movie_id.append(i["id"])
    response3 = {}
    for i in movie_id:
        response3[i] = requests.get(apiBaseURL + 'movie/' + str(i) + '?api_key=' + apiKey).json()
    return render(request, 'searchresults.html/', {'response3' : response3})

   
def review(request):
    
    movieid = request.POST.get("movieid")
    title = request.POST.get(requests.get(apiBaseURL + 'movie/' + movieid + '?api_key=' + apiKey).json()["title"])
    overview = request.POST.get(requests.get(apiBaseURL + 'movie/' + movieid + '?api_key=' + apiKey).json()["overview"])
    rating = request.POST.get(requests.get(apiBaseURL + 'movie/' + movieid + '?api_key=' + apiKey).json()["vote_average"])
    release = request.POST.get(requests.get(apiBaseURL + 'movie/' + movieid + '?api_key=' + apiKey).json()["release_date"])
    moviedata = movies(movieid=movieid, title=title, overview=overview, rating=rating, release=release)
    moviedata.save()
    
    return render(request, 'review.html')
        