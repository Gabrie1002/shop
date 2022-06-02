from django.contrib import admin
from apps.catalog.models import *


class SubcategoryInLine(admin.TabularInline):
    model = Subcategory
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'slug', 'publish']
    inlines = [SubcategoryInLine, ]


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'slug', 'publish']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'slug', 'publish']


class PriceInLine(admin.TabularInline):
    model = Price
    extra = 0


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'slug', 'publish']


@admin.register(PriceType)
class PriceType(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'slug', 'publish']


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ['product', 'price_type', 'price', 'publish']


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'slug', 'subcategory', 'has_sale', 'publish']
    filter_horizontal = ['colors']
    inlines = [PriceInLine, ProductImageInLine, ]
