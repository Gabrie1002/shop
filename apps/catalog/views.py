from django.shortcuts import render
from apps.catalog.models import Category
from django.http import Http404


def categories(request):
    context = {}
    categories = Category.objects.filter(publish=True)
    context['categories'] = categories
    return render(request, 'catalog/categories.html', context)


def subcategories(request, slug):
    context = {}
    if Category.objects.filter(publish=True, slug=slug).exists():
        category = Category.objects.get(publish=True, slug=slug)
        context['category'] = category
        context['subcategory'] = category.subcategory.filter(publish=True)
    else:
        raise Http404
    return render(request, 'catalog/subcategories.html', context)


def products(request, category_slug, subcatogory_slug):
    context = {}

    return render(request, 'catalog/products.html', context)
