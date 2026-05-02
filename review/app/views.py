from django.shortcuts import render, redirect, get_object_or_404

from .models import Movie, Review

from .forms import MovieForm, ReviewForm


# MOVIE LIST
def movie_list(request):

    movies = Movie.objects.all()

    return render(request, 'movie_list.html', {
        'movies': movies
    })


# ADD MOVIE
def add_movie(request):

    form = MovieForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('movie_list')

    return render(request, 'add_movie.html', {
        'form': form
    })


# MOVIE DETAIL + REVIEW
def movie_detail(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    reviews = Review.objects.filter(movie=movie)

    form = ReviewForm(request.POST or None)

    if form.is_valid():

        review = form.save(commit=False)

        review.movie = movie

        review.save()

        return redirect('movie_detail', movie_id=movie.id)

    return render(request, 'movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'form': form
    })