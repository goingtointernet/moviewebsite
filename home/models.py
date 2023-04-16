from django.db import models

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
    title = models.CharField(max_length=160)
    description = models.CharField(max_length=160)
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
    movie_stream_link = models.CharField(max_length=160)
    download_links = models.ManyToManyField(DownloadLink, blank=True)
    permalink =models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Movie.objects.get(id=self.id)
            if this.movie_thumb != self.movie_thumb:
                this.movie_thumb.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Movie, self).save(*args, **kwargs)



class MovieSlider(models.Model):
    slide_movies = models.ManyToManyField(Movie, blank=True)