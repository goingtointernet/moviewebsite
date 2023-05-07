"""moviesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #add this
from django.conf.urls.static import static #add this
from django.conf import settings
from django.views.static import serve
from django.urls import re_path as url
from django.contrib.sitemaps.views import sitemap

from home.sitemap import PostSitemap, PageSitemap
from django.views.generic.base import TemplateView 

sitemaps = {
    'posts': PostSitemap,
    'pages': PageSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path("robots.txt",TemplateView.as_view(template_name="seo/robots.txt", content_type="text/plain")),  #add the robots.txt file
    path("ads.txt",TemplateView.as_view(template_name="seo/ads.txt", content_type="text/plain")),  #add the ads.txt file
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404= 'home.views.error_404_view'