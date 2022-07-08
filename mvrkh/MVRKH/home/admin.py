from django.contrib import admin
from . models import movies, user, reviews
# Register your models here.

admin.site.register(movies)
admin.site.register(reviews)
admin.site.register(user)
