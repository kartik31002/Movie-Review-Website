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
    
    def __str__(self):
        return self.title

class user(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    email.primary_key = True
    
    def __str__(self):
        return self.username

class reviews(models.Model):
    movieid = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    review = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.username