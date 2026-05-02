from django.urls import path

from . import views


urlpatterns = [

    path('', views.movie_list, name='movie_list'),

    path('add-movie/', views.add_movie, name='add_movie'),

    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]