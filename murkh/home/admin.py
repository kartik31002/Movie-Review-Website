from django.contrib import admin
from . models import movies, reviews, user
# Register your models here.

admin.site.register(movies)
admin.site.register(reviews)
admin.site.register(user)

