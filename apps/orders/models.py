from django.db import models
from django.utils import timezone
from apps.catalog.models import Product, Color
from apps.profile.models import Profile


class Order(models.Model):
    datetime = models.DateTimeField('datetime', default=timezone.now)
    profile = models.ForeignKey(Profile, related_name='profile_orders', on_delete=models.CASCADE)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_order_details', on_delete=models.CASCADE)
    count = models.IntegerField('count', default=1)
    color = models.ForeignKey(Color, related_name='color_order_details', on_delete=models.CASCADE)
    price = models.FloatField('price', default=0)