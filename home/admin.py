from django.contrib import admin
from .models import Category, Movie, DownloadLink, MovieSlider
# Movie
@admin.register(Movie)
class MovieModelAdmin(admin.ModelAdmin):
    list_display = ['title','imb_rating','movie_language','movie_duration']
# Category
admin.site.register(Category)
#Download Links
admin.site.register(DownloadLink)
#slider
admin.site.register(MovieSlider)
