from django.conf import settings
from .models import SiteData, Ads, Menu, StaticPosts

#Site Data
def sitedata(request):
    sitedata = SiteData.objects.all().first()
    return {"sitedata": sitedata}

#Ads Data
def ads(request):
    ads = Ads.objects.all().first()
    return {"ads": ads}

#Menu
def menu(request):
    menu = Menu.objects.all().order_by('-pk')
    return {"menu": menu}

#pages
def pages(request):
    pages = StaticPosts.objects.all().order_by('-pk')
    return {"pages": pages}