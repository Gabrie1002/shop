from django.urls import path
from apps.catalog import views


urlpatterns = [
    path('catalog/', views.categories, name='categories'),
    path('catalog/products/<str:slug>/', views.product_item, name='product_item'),
    path('catalog/collection/<str:slug>/', views.collection, name='collection'),
    path('catalog/color/<str:slug>/', views.color, name='color'),
    path('catalog/material/<str:slug>/', views.material, name='material'),
    path('catalog/<str:slug>/', views.subcategories, name='subcategories'),
    path('catalog/<str:category_slug>/<str:subcategory_slug>/', views.products, name='products'),
]