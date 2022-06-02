from django.shortcuts import render
from apps.catalog.models import Category, Subcategory, Product, Collection, Color, Material
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


def products(request, category_slug, subcategory_slug):
    context = {}
    if Category.objects.filter(publish=True, slug=category_slug).exists():
        category = Category.objects.get(publish=True, slug=category_slug)
        context['category'] = category
    else:
        raise Http404

    if Subcategory.objects.filter(publish=True, slug=subcategory_slug).exists():
        category = Subcategory.objects.get(publish=True, slug=subcategory_slug)
        context['subcategory'] = category
    else:
        raise Http404

    products = Product.objects.filter(publish=True, subcategory__slug=subcategory_slug)
    context['products'] = products
    context['materials'] = Material.objects.filter(publish=True)
    context['colors'] = Color.objects.filter(publish=True)
    context['collections'] = Collection.objects.filter(publish=True)

    return render(request, 'catalog/products.html', context)


def collection(request, slug):
    context = {}
    if not Collection.objects.filter(publish=True, slug=slug).exists():
        raise Http404
    products = Product.objects.filter(publish=True, collection__slug=slug)
    context['products'] = products
    context['materials'] = Material.objects.filter(publish=True)
    context['colors'] = Color.objects.filter(publish=True)
    context['collections'] = Collection.objects.filter(publish=True)
    return render(request, 'catalog/products.html', context)


def material(request, slug):
    context = {}
    if not Material.objects.filter(publish=True, slug=slug).exists():
        raise Http404
    products = Product.objects.filter(publish=True, material__slug=slug)
    context['products'] = products
    context['materials'] = Material.objects.filter(publish=True)
    context['colors'] = Color.objects.filter(publish=True)
    context['collections'] = Collection.objects.filter(publish=True)
    return render(request, 'catalog/products.html', context)


def color(request, slug):
    context = {}
    if not Color.objects.filter(publish=True, slug=slug).exists():
        raise Http404
    products = Product.objects.filter(publish=True, colors__slug=slug)
    context['products'] = products
    context['materials'] = Material.objects.filter(publish=True)
    context['colors'] = Color.objects.filter(publish=True)
    context['collections'] = Collection.objects.filter(publish=True)
    return render(request, 'catalog/products.html', context)
