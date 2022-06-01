from django.contrib import admin
from django.urls import path, include
from apps.catalog import views


urlpatterns = [
    path('catalog/', views.categories, name='categories'),
    path('catalog/<str:slug>/', views.subcategories, name='subcategories'),
    path('catalog/<str:category_slug>/<str:subcatogory_slug>/', views.products, name='products'),
]