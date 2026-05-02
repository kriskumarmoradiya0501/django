from django.urls import path

from . import views


urlpatterns = [

    path('', views.product_list, name='product_list'),

    path('add-product/', views.add_product, name='add_product'),

    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    path('api/categories/', views.category_list),

    path('api/create-category/', views.create_category),

    path('api/category/<int:category_id>/', views.category_detail),

    path('api/update-category/<int:category_id>/', views.update_category),
]