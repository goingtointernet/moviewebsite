from django.shortcuts import render
from .models import Movie, MovieSlider
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    p = Paginator(Movie.objects.all().order_by('-pk'),10)
    page = request.GET.get('page')
    pagination = p.get_page(page)
    current_numer = pagination.number
    total_number = pagination.paginator.num_pages
    if current_numer == total_number and current_numer != 0:
        current_numer = current_numer - 1
    if total_number == 1:
         page_range = 1
    else:
        page_range =(current_numer, total_number)
    slider = MovieSlider.objects.all().first()
    return render(request,'home/index.html', {'slider':slider, 'pagination':pagination, 'page_range':page_range})

def moviepost(request, permalink):
    moviedetails = Movie.objects.filter(permalink=permalink).first()
    relaated_category = moviedetails.movie_categories.all()
    relaated_movie = []
    for relaated_category in relaated_category:
        relaated_category.counter = Movie.objects.filter(movie_categories=relaated_category)
        relaated_movie += relaated_category.counter
    r_movie = list(dict.fromkeys(relaated_movie))
    r_movie.remove(moviedetails)
    if moviedetails:
        context = {'moviedetails':moviedetails,'r_movie':r_movie}
        return render(request, 'home/movie-details.html', context)
    else:
        return render(request, 'home/404.html')

#==custome-404===============================# 
def error_404_view(request, exception):
    return render(request, 'home/404.html')

#==Search============================#
def search(request):
    search=request.GET['search']
    if len(search)>78:
        movie = []
        search = "Search To Large!"
    else:    
        movie_title = Movie.objects.filter(title__icontains=search)
        movie_category = Movie.objects.filter(movie_categories__name__icontains=search)
        #movie = movie_title.union(movie_category)


        p = Paginator(movie_title.union(movie_category).order_by('-pk'), 10)
        page = request.GET.get('page')
        pagination = p.get_page(page)
        current_numer = pagination.number
        total_number = pagination.paginator.num_pages
        if current_numer == total_number and current_numer != 0:
            current_numer = current_numer - 1
        if total_number == 1:
             page_range = 1
        else:
            page_range =(current_numer, total_number)


    params={'pagination': pagination,'search':search, 'page_range':page_range}
    return render(request, 'home/search.html', params)