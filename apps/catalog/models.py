from django.db import models


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


class Material(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    category = models.ForeignKey(
        Category,
        related_name='category_products',
        on_delete=models.CASCADE
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


class PriceType(models.Model):
    title = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    publish = models.BooleanField('publish', default=True)

    def __str__(self):
        return self.title


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
