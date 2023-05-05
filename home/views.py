from django.shortcuts import render
from .models import Movie, MovieSlider, HomeSections
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def index(request):
    p = Paginator(Movie.objects.all().order_by('-pk'),20)

    home_sections = HomeSections.objects.all()
    allmovie = Movie.objects.all().order_by('-pk')

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
    return render(request,'home/index.html', {'allmovie':allmovie,'home_sections':home_sections, 'slider':slider, 'pagination':pagination, 'page_range':page_range})

def moviepost(request, permalink):
    moviedetails = Movie.objects.filter(permalink=permalink).first()
    relaated_movie = []
    if moviedetails:
        relaated_category = moviedetails.movie_categories.all()
        for relaated_category in relaated_category:
            relaated_category.counter = Movie.objects.filter(movie_categories=relaated_category)
            relaated_movie += relaated_category.counter
        r_movie = list(dict.fromkeys(relaated_movie))
        r_movie.remove(moviedetails)
        context = {'moviedetails':moviedetails,'r_movie':r_movie}
        return render(request, 'home/movie-details.html', context)
    else:
        return render(request, 'home/404.html')

#==custome-404===============================# 
def error_404_view(request, exception):
    return render(request, 'home/404.html')

#==Search============================#
def search(request):
    search = request.GET.get('search')
    page_range = None
    pagination = None

    if search == None:
        return render(request, 'home/404.html')
    elif len(search)>78:
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



def movie_request(request):
    message_success = None
    error = None
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            movie_name = request.POST.get('movie_name')
        except:
            name = ""
            email = ""
            movie_name = ""
        data = {
            'movie':movie_name,
            'name':name,
            'email':email,
        }
        message = '''
        Movie Name: {}
        User Name: {}
        User Email: {}
        '''.format(data['movie'],data['name'],data['email'])
        if name != "" and email != "" and movie_name != "" and name != None and email != None and movie_name != None:
            try:
                send_mail('Movie Request From User', message, '',['gmovie1264@gmail.com'])
                message_success = "*Request Sent Successfully"
            except:
                error="*Please Enter Valid Values"

        else:
            error="*Please Fill All Fields Correctly"
    return render(request, 'home/request.html',{"message_success":message_success,"error":error})