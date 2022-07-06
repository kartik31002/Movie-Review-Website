import json
from django.shortcuts import render, HttpResponse
import requests

apiBaseURL = 'https://api.themoviedb.org/3/'
apiKey = '3d9b4ef8cf0ea93474001f18dabe2e00'

imageBaseUrl = 'https://image.tmdb.org/t/p/'

# Create your views here.
def index(request):
    response = requests.get(apiBaseURL + 'movie/now_playing?api_key=' + apiKey).json()
    # popular_dict = json.loads(response)
    popular_movies = response["results"]
    movie_id = []
    for i in popular_movies:
        movie_id.append(i["id"])
    response2 = []
    for i in movie_id:
        response2.append(requests.get(apiBaseURL + 'movie/' + str(i) + '?api_key=' + apiKey).json())
    return render(request, 'index.html', response2)