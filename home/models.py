from django.db import models
from django.urls import reverse
from io import BytesIO
import sys
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
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
    stream_total_episode = models.IntegerField(null=True, blank=True)
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
            if this.movie_screenshot1 != self.movie_screenshot1:
                this.movie_screenshot1.delete(save=False)
            if this.movie_screenshot2 != self.movie_screenshot2:
                this.movie_screenshot2.delete(save=False)
            if this.movie_screenshot3 != self.movie_screenshot3:
                this.movie_screenshot3.delete(save=False)
            if this.movie_screenshot4 != self.movie_screenshot4:
                this.movie_screenshot4.delete(save=False)
            if this.movie_cover != self.movie_cover:
                this.movie_cover.delete(save=False)        
        
            if  this.movie_thumb != self.movie_thumb:
                # Opening the uploaded image
                im = Image.open(self.movie_thumb)
                output = BytesIO()
                #=================
                basewidth = 350
                wpercent = (basewidth/float(im.size[0]))
                hsize = int((float(im.size[1])*float(wpercent)))
                # Resize/modify the image
                im = im.resize((basewidth, hsize))
                # after modifications, save it to the output
                im.save(output, format='JPEG', quality=90)
                output.seek(0)
                # change the imagefield value to be the newley modifed image value
                self.movie_thumb = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.movie_thumb.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

            if  this.movie_cover != self.movie_cover:
                # Opening the uploaded image
                im2 = Image.open(self.movie_cover)
                output2 = BytesIO()
                #=================
                basewidth2 = 1000
                wpercent2 = (basewidth2/float(im2.size[0]))
                hsize2 = int((float(im2.size[1])*float(wpercent2)))
                # Resize/modify the image
                im2 = im2.resize((basewidth2, hsize2))
                # after modifications, save it to the output
                im2.save(output2, format='JPEG', quality=90)
                output2.seek(0)
                # change the imagefield value to be the newley modifed image value
                self.movie_cover = InMemoryUploadedFile(output2, 'ImageField', "%s.jpg" % self.movie_cover.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output2), None)
            #screen 1
            if  this.movie_screenshot1 != self.movie_screenshot1:
                # Opening the uploaded image
                ims1 = Image.open(self.movie_screenshot1)
                outputs1 = BytesIO()
                #=================
                basewidths1 = 400
                wpercents1 = (basewidths1/float(ims1.size[0]))
                hsizes1 = int((float(ims1.size[1])*float(wpercents1)))
                # Resize/modify the image
                ims1 = ims1.resize((basewidths1, hsizes1))
                # after modifications, save it to the output
                ims1.save(outputs1, format='JPEG', quality=90)
                outputs1.seek(0)
                # change the imagefield value to be the newley modifed image value
                self.movie_screenshot1 = InMemoryUploadedFile(outputs1, 'ImageField', "%s.jpg" % self.movie_screenshot1.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(outputs1), None)

            #screen 2
            if  this.movie_screenshot2 != self.movie_screenshot2:
                # Opening the uploaded image
                ims2 = Image.open(self.movie_screenshot2)
                outputs2 = BytesIO()
                #=================
                basewidths2 = 400
                wpercents2 = (basewidths2/float(ims2.size[0]))
                hsizes2 = int((float(ims2.size[1])*float(wpercents2)))
                # Resize/modify the image
                ims2 = ims2.resize((basewidths2, hsizes2))
                # after modifications, save it to the output
                ims2.save(outputs2, format='JPEG', quality=90)
                outputs2.seek(0)
                # change the imagefield value to be the newley modifed image value
                self.movie_screenshot2 = InMemoryUploadedFile(outputs2, 'ImageField', "%s.jpg" % self.movie_screenshot2.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(outputs2), None)
                
            #screen 3
            if  this.movie_screenshot3 != self.movie_screenshot3:
                # Opening the uploaded image
                ims3 = Image.open(self.movie_screenshot3)
                outputs3 = BytesIO()
                #=================
                basewidths3 = 400
                wpercents3 = (basewidths3/float(ims3.size[0]))
                hsizes3 = int((float(ims3.size[1])*float(wpercents3)))
                # Resize/modify the image
                ims3 = ims3.resize((basewidths3, hsizes3))
                # after modifications, save it to the output
                ims3.save(outputs3, format='JPEG', quality=90)
                outputs3.seek(0)
                # change the imagefield value to be the newley modifed image value
                self.movie_screenshot3 = InMemoryUploadedFile(outputs3, 'ImageField', "%s.jpg" % self.movie_screenshot3.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(outputs3), None)
                

            #screen 4
            if  this.movie_screenshot4 != self.movie_screenshot4:
                # Opening the uploaded image
                ims4 = Image.open(self.movie_screenshot4)
                outputs4 = BytesIO()
                #=================
                basewidths4 = 400
                wpercents4 = (basewidths4/float(ims4.size[0]))
                hsizes4 = int((float(ims4.size[1])*float(wpercents4)))
                # Resize/modify the image
                ims4 = ims4.resize((basewidths4, hsizes4))
                # after modifications, save it to the output
                ims4.save(outputs4, format='JPEG', quality=90)
                outputs4.seek(0)
                # change the imagefield value to be the newley modifed image value
                self.movie_screenshot4 = InMemoryUploadedFile(outputs4, 'ImageField', "%s.jpg" % self.movie_screenshot4.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(outputs4), None)

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
    def __str__(self):
        return self.section_heading
# Static-Pages.
class StaticPosts(models.Model):
    title = models.CharField(max_length=160)
    meta_desc = models.CharField(max_length=160)
    meta_key = models.CharField(max_length=260)
    page_name = models.CharField(max_length=70)
    content = models.TextField()
    permalink = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("moviepost",args=[self.permalink])