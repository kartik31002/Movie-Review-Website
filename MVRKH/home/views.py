import json
from urllib import response
from django.shortcuts import render, HttpResponse
import requests
from django.contrib import messages
from . models import movies, user, reviews
from datetime import datetime



# Create your views here.

apiBaseURL = 'https://api.themoviedb.org/3/'
apiKey = '3d9b4ef8cf0ea93474001f18dabe2e00'

def index(request):
    response = requests.get(apiBaseURL + 'movie/now_playing?api_key=' + apiKey).json()
    popular_movies = response["results"]
    movie_id = []
    for i in popular_movies:
        movie_id.append(i["id"])
    response3 = {}
    for i in movie_id:
        response3[i] = requests.get(apiBaseURL + 'movie/' + str(i) + '?api_key=' + apiKey).json()
    return render(request, 'index.html', {'response3' : response3, 'title' : 'Home'})

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
    return render(request, 'index.html/', {'response3' : response3, 'title' : searchTerm})

def genre(request):
    genreid = request.POST.get("genreid")
    if (genreid == "0"):
        response = requests.get(apiBaseURL + 'movie/now_playing?api_key=' + apiKey).json()
    else:
        response = requests.get(apiBaseURL + 'genre/' + genreid + '/movies?api_key=' + apiKey + '&language=en-US&include_adult=false&sort_by=created_at.asc').json()
    popular_movies = response["results"]
    movie_id = []
    for i in popular_movies:
        movie_id.append(i["id"])
    response3 = {}
    for i in movie_id:
        response3[i] = requests.get(apiBaseURL + 'movie/' + str(i) + '?api_key=' + apiKey).json()
    return render(request, 'index.html/', {'response3' : response3, 'title' : 'Genre'})

def review(request):

    movie_id = request.POST.get("movieid")
    response = requests.get(apiBaseURL + 'movie/' + movie_id + '?api_key=' + apiKey).json()
    title = response["title"]
    overview = response["overview"]
    rating = response["vote_average"]
    release = response["release_date"]
    moviedata = movies(movieid=movie_id, title=title, overview=overview, rating=rating, release=release)
    moviedata.save()
    review = reviews.objects.all().filter(movieid = movie_id)
    return render(request, 'review.html', {'response':response, 'review':review})

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        if user.objects.filter(email=email): 
            messages.error(request, 'Email already Exists!')
            return render(request, 'signup.html')
        elif user.objects.filter(username=username):
            messages.error(request, 'Username already Exists!')
            return render(request, 'signup.html')
        else:
            User = user(username=username, email=email)
            User.save()
            messages.success(request, 'User registered!')
            response = requests.get(apiBaseURL + 'movie/now_playing?api_key=' + apiKey).json()
            popular_movies = response["results"]
            movie_id = []
            for i in popular_movies:
                movie_id.append(i["id"])
            response3 = {}
            for i in movie_id:
                response3[i] = requests.get(apiBaseURL + 'movie/' + str(i) + '?api_key=' + apiKey).json()
            return render(request, 'index.html', {'response3' : response3, 'title' : 'Home'})
    else:    
        return render(request, 'signup.html')

def write(request):
        movie_id = request.POST.get("movieid")
        response = requests.get(apiBaseURL + 'movie/' + str(movie_id) + '?api_key=' + apiKey).json()
        return render(request, 'write.html', {'response':response})
    
def written(request):
    movie_id = request.POST.get("movieid")
    movieidobj = movies.objects.filter(movieid=str(movie_id))
    response = requests.get(apiBaseURL + 'movie/' + str(movie_id) + '?api_key=' + apiKey).json()
    user_name = request.POST.get("username")
    movie_review = request.POST.get("review")
    if user.objects.filter(username = user_name).exists():
        reviews.objects.create(movieid=str(movie_id), username=user_name, review=movie_review, date=datetime.today())
        messages.success(request, 'Review written!')
        return render(request, 'review.html', {'response':response})
    else:
        messages.error(request, "User isn't registered!")
        return render(request, 'write.html', {'response':response})
