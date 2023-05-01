from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search',views.search, name='search'),
    path('movie-request',views.movie_request, name='movie_request'),
    path('<str:permalink>',views.moviepost, name='moviepost'),
    ]