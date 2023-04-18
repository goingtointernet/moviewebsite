from django.contrib.sitemaps import Sitemap
from .models import Movie

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Movie.objects.all()