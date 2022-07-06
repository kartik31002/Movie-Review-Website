from django.db import models

# Create your models here.

class movies(models.Model):
    movieid = models.IntegerField()
    title = models.CharField(max_length=1000)
    overview = models.CharField(max_length=1000)
    rating = models.FloatField()
    release = models.DateField()
    
