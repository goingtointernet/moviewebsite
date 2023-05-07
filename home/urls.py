from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search',views.search, name='search'),
    path('movie-request',views.movie_request, name='movie_request'),
    path('contact-us',views.contact, name='contact'),
    path('latest-movies',views.latest, name='latest'),
    path('<str:permalink>',views.moviepost, name='moviepost'),
    ]