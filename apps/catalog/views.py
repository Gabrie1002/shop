from django.shortcuts import render
from apps.catalog.models import Category, Subcategory, Product, Collection, Color, Material
from django.http import Http404
from django.core.paginator import Paginator
from apps.catalog.forms import ProductForm
from apps.orders.models import Order, OrderDetails
from django.contrib.sessions.models import Session


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
    context['products'] = paginator_get_page(request, products)
    context['materials'] = Material.objects.filter(publish=True)
    context['colors'] = Color.objects.filter(publish=True)
    context['collections'] = Collection.objects.filter(publish=True)

    return render(request, 'catalog/products.html', context)


def collection(request, slug):
    context = {}
    if not Collection.objects.filter(publish=True, slug=slug).exists():
        raise Http404
    products = Product.objects.filter(publish=True, collection__slug=slug)
    context['products'] = paginator_get_page(request, products)
    context['materials'] = Material.objects.filter(publish=True)
    context['colors'] = Color.objects.filter(publish=True)
    context['collections'] = Collection.objects.filter(publish=True)
    return render(request, 'catalog/products.html', context)


def material(request, slug):
    context = {}
    if not Material.objects.filter(publish=True, slug=slug).exists():
        raise Http404
    products = Product.objects.filter(publish=True, material__slug=slug)
    context['products'] = paginator_get_page(request, products)
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


def paginator_get_page(request, products):
    paginator = Paginator(products, 9)

    page = request.GET.get('page')
    products = paginator.get_page(page)
    return products


def product_item(request, slug):
    context = {}

    if Product.objects.filter(slug=slug, publish=True).exists():
        product = Product.objects.filter(slug=slug, publish=True).last()
        context['product'] = product
    else:
        raise Http404

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            order = get_current_order(request)

            color = form.cleaned_data['color']
            count = form.cleaned_data['count']
            size = form.cleaned_data['size']
            if order.details.filter(product=product, color=color, size=size).exists():
                order_details = order.details.filter(product=product, color=color, size=size).first()
                order_details.count += count
                order_details.save()

            else:
                order_details = OrderDetails()
                order_details.order = order
                order_details.count = count
                order_details.product = product
                order_details.size = size
                order_details.color = color
                order_details.price = product.current_price()
                order_details.save()
        context['success'] = True
        context['form'] = ProductForm()
    else:

        context['form'] = ProductForm()
    return render(request, 'catalog/product_item.html', context)


def get_current_order(request):
    if Order.objects.filter(session__session_key=request.session.session_key, status__isnull=True):
        return Order.objects.filter(session__session_key=request.session.session_key, status__isnull=True).first()
    else:
        order = Order()

        if not request.session.session_key:
            request.session.save()

        session = Session.objects.get(session_key=request.session.session_key)

        order.session = session
        order.save()
        return order
