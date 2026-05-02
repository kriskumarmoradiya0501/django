from django.urls import path

from . import views


urlpatterns = [

    path('', views.doctor_list, name='doctor_list'),

    path('add-doctor/', views.add_doctor, name='add_doctor'),

    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),

    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),
]