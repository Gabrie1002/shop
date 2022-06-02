from django.db import models
from colorfield.fields import ColorField


class Category(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    image = models.ImageField('image', upload_to='categories', blank=True, null=True)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/catalog/%s/' % self.slug


class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    image = models.ImageField('image', upload_to='subcategories', blank=True, null=True)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/catalog/%s/%s/' % (self.category.slug, self.slug)


class Collection(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/catalog/collection/%s/' % self.slug


class Material(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/catalog/material/%s/' % self.slug


class Color(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    publish = models.BooleanField('publish', default=True)
    color = ColorField(default='FF0000')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/catalog/color/%s/' % self.slug


class PriceType(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    subcategory = models.ForeignKey(
        Subcategory,
        related_name='subcategory_products',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    collection = models.ForeignKey(
        Collection,
        related_name='collection_products',
        on_delete=models.CASCADE
    )
    material = models.ForeignKey(
        Material,
        related_name='material_products',
        on_delete=models.CASCADE
    )
    colors = models.ManyToManyField(Color, related_name='colors_products')
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']

    def cover_image(self):
        if self.product_images.exists():
            return self.product_images.first().image

    def has_sale(self):
        if self.product_prices.filter(price_type__slug='sale', publish=True).exists():
            return True
        return False

    def get_regular_price(self):
        if self.product_prices.filter(price_type__slug='regular', publish=True).exists():
            return self.product_prices.filter(price_type__slug='regular', publish=True).last().price

    def get_sale_price(self):
        if self.product_prices.filter(price_type__slug='sale', publish=True).exists():
            return self.product_prices.filter(price_type__slug='sale', publish=True).last().price


class Price(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='product_prices',
        on_delete=models.CASCADE
    )
    price_type = models.ForeignKey(
        PriceType,
        related_name='price_type_prices',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    price = models.FloatField('price')
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.product.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE)
    image = models.ImageField('image', upload_to='products')

    def __str__(self):
        return self.product.title
