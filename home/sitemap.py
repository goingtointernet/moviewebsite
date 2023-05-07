from django.contrib.sitemaps import Sitemap
from .models import Movie, StaticPosts

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Movie.objects.all()
    
class PageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return StaticPosts.objects.all()