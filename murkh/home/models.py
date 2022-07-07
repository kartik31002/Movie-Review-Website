import email
from tkinter import CASCADE
from django.db import models

# Create your models here.

class movies(models.Model):
    movieid = models.CharField(max_length=20)
    title = models.CharField(max_length=1000)
    overview = models.TextField()
    rating = models.CharField(max_length=10)
    release = models.DateField()
    movieid.primary_key = True

class user(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100,)
    password = models.CharField(max_length=16)
    email.primary_key = True

class reviews(models.Model):
    movieid = models.ForeignKey('movies', on_delete = models.CASCADE)
    email = models.ForeignKey('user', on_delete = models.CASCADE)
    review = models.TextField()