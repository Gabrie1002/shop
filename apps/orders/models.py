from django.db import models
from django.utils import timezone
from apps.catalog.models import Product, Color, Size
from apps.profile.models import Profile
from django.contrib.sessions.models import Session


class Status(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug')

    def __str__(self):
        return self.title


class Order(models.Model):
    datetime = models.DateTimeField('datetime', default=timezone.now)
    profile = models.ForeignKey(Profile, related_name='profile_orders', on_delete=models.CASCADE, blank=True, null=True)
    session = models.ForeignKey(Session, related_name='session_orders', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField('name', max_length=255, blank=True, null=True)
    email = models.EmailField('email', max_length=255, blank=True, null=True)
    phone = models.CharField('phone', max_length=255, blank=True, null=True)
    country = models.CharField('country', max_length=255, blank=True, null=True)
    city = models.CharField('city', max_length=255, blank=True, null=True)
    address = models.CharField('address', max_length=255, blank=True, null=True)
    status = models.ForeignKey(Status, related_name='status_orders', on_delete=models.CASCADE, blank=True, null=True)


    def get_total(self):
        total = 0
        for detail in self.details.all():
            total += detail.get_total()
        return total


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_order_details', on_delete=models.CASCADE)
    count = models.IntegerField('count', default=1)
    color = models.ForeignKey(Color, related_name='color_order_details', on_delete=models.CASCADE)
    price = models.FloatField('price', default=0)
    size = models.ForeignKey(Size, related_name='size_order_details', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.product.title

    def get_total(self):
        total = self.count * self.price
        return total