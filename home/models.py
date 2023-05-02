from django.db import models
from django.urls import reverse

# Category
class Category(models.Model):
    name = models.CharField(max_length=160, unique= True)
    
    def __str__(self):
        return self.name
    
    

# Category
class DownloadLink(models.Model):
    name = models.CharField(max_length=160, unique= False)
    resolution = models.CharField(max_length=160, unique= False)
    link = models.CharField(max_length=160, unique= False)
    
    def __str__(self):
        return self.name

# Movie
class Movie(models.Model):
    meta_title = models.CharField(max_length=160, default='')
    meta_description = models.CharField(max_length=160, default='')
    title = models.CharField(max_length=160)
    description = models.TextField(max_length=1000, default='')
    keyword = models.CharField(max_length=160, default='')
    movie_thumb = models.ImageField(upload_to='movie_thumb')
    movie_cover = models.ImageField(upload_to='movie_cover', null=True)
    movie_categories = models.ManyToManyField(Category, blank=True)
    movie_screenshot1 = models.ImageField(upload_to='movie_screenshot')
    movie_screenshot2 = models.ImageField(upload_to='movie_screenshot')
    movie_screenshot3 = models.ImageField(upload_to='movie_screenshot')
    movie_screenshot4 = models.ImageField(upload_to='movie_screenshot')
    imb_rating = models.FloatField()
    movie_pulished_date = models.DateField()
    movie_duration = models.CharField(max_length=80)
    movie_quality = models.CharField(max_length=80, default="HD")
    movie_language = models.CharField(max_length=160)
    movie_trailer_link = models.CharField(max_length=160)
    movie_imdb_id = models.CharField(max_length=260, default="", null=True, blank=True)
    movie_tmbd_id = models.CharField(max_length=260, default="", null=True, blank=True)
    stream_movie_or_show_title = models.CharField(max_length=260, default="", null=True, blank=True)
    stream_movie_or_show_year = models.IntegerField(null=True, blank=True)
    stream_season_number = models.IntegerField(null=True, blank=True)
    stream_episode_number = models.IntegerField(null=True, blank=True)
    movie_stream_cutome_link = models.CharField(max_length=260, default="", null=True, blank=True)
    download_links = models.ManyToManyField(DownloadLink, blank=True)
    permalink =models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("moviepost",args=[self.permalink])

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Movie.objects.get(id=self.id)
            if this.movie_thumb != self.movie_thumb:
                this.movie_thumb.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Movie, self).save(*args, **kwargs)



class MovieSlider(models.Model):
    slider_heading = models.CharField(max_length=260, default="")
    slide_movies = models.ManyToManyField(Movie, blank=True)

# Site-Data.
class SiteData(models.Model):
    logo = models.CharField(max_length=160, default="Movies")
    fav_icon = models.ImageField( upload_to = 'logo', null = True, blank = True)
    site_name = models.CharField(max_length=100, default='')
    title = models.CharField(max_length=100, default='')
    slider_box_height = models.CharField(max_length=100, default='450px')
    latest_post_section_heading = models.CharField(max_length=100, default='Latest Movies')
    movie_box_height = models.CharField(max_length=100, default='550px')
    movie_banner_min_height = models.CharField(max_length=100, default='520px')
    meta_description = models.CharField(max_length=150, default='')
    meta_keyword = models.CharField(max_length=200, default='')
    site_url = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=160, default="")
    facebook = models.CharField(max_length=160,  default="", blank=True, null=True)
    instagram = models.CharField(max_length=160,  default="", blank=True, null=True)
    twitter = models.CharField(max_length=160,default="", blank=True, null=True)
    author = models.CharField(max_length=160,default="", blank=True, null=True)
    made_by = models.CharField(max_length=160,default="")
    copyright = models.CharField(max_length=160,default="")
    custome_css = models.TextField(default="", blank=True, null=True)
    head_script = models.TextField(default="", blank=True, null=True)
    bodyend_script = models.TextField(default="", blank=True, null=True)
    show_ads= models.BooleanField('show all ad', default=False)

class Ads(models.Model):
    head_ad = models.TextField(default="")
    simple_content_ad = models.TextField(default="")
    footer_ad = models.TextField(default="")
    fixed_ad = models.TextField(default="")
    show_fixed_ad = models.BooleanField('show fixed ad', default=False)


# Menu
class Menu(models.Model):
    name = models.CharField(max_length=160, default="")
    def __str__(self):
        return self.name
    
class HomeSections(models.Model):
    section_heading = models.CharField(max_length=160, default="")
    selected_movies = models.ManyToManyField(Movie, blank=True)
    movies_by_category = models.OneToOneField(Category, blank=True, null=True, default="None", on_delete=models.SET_NULL)