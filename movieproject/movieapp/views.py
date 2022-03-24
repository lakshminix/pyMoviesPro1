from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movie1 = movie.objects.all()
    context = {
        'movie_list': movie1
    }
    return render(request, 'movie.html', context)


def detail(request, movie_id):
    mf = movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'result': mf})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        descr = request.POST.get('descr')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie2=movie(name=name,descr=descr,year=year,img=img)
        movie2.save()
    return render(request, 'add.html')

def update(request,id):
    movies = movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'forms':form,'movies':movies})

def delete(request,id):
    if request.method=='POST':
        movies = movie.objects.get(id=id)
        movies.delete()
        return redirect('/')

    return render(request,'delete.html')



