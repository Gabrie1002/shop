from django.urls import path
from apps.orders import views


urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart/checkout', views.checkout, name='checkout'),

    path('cart/delete_product/<int:pk>/', views.delete_product, name='delete_product'),

]