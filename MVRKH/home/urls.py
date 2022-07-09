from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index.html/', views.index, name='home'),
    path('signup/', views.signup, name='Sign In'),
    # path('registered/', views.registered, name='Registered'),
    path('review/', views.review, name='review'),
    path('searchresults/', views.searchresults, name='searchresults'),
    path('genre/', views.genre, name='genre'),
    path('write/', views.write, name='write'),
    path('written/', views.written, name='written'),
]