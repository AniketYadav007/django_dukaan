from django.urls import path
from . import views

urlpatterns =[
    path('product/all', views.all_products, name='all_products'),
    path('product/<slug:brand>/all/', views.brand_products, name='brand_products'),
    path('product/<slug:category>/all/', views.category_products, name='category_products'),
    path('product/<slug:brand>/<slug:category>/all/', views.brand_category_products, name='brand_category_products'),

    #searching products
    path('product/search/', views.search_products, name='search_products'),
]