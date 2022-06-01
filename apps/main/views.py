from django.shortcuts import render
from apps.main.models import Page
from django.http import Http404


def index(request):
    return render(request, 'index.html')


def about(request):
    context = {}
    page = Page.objects.get(slug='about')
    context['page'] = page
    return render(request, 'page.html', context)


def mission(request):
    context = {}
    if Page.objects.filter(slug='mission').exists():
        page = Page.objects.get(slug='mission')
    else:
        raise Http404
    context['page'] = page
    return render(request, 'page.html', context)


def contacts(request):
    context = {}
    if Page.objects.filter(slug='contacts').exists():
        page = Page.objects.get(slug='contacts')
    else:
        raise Http404
    context['page'] = page
    return render(request, 'page.html', context)


def requisites(request):
    context = {}
    if Page.objects.filter(slug='requisites').exists():
        page = Page.objects.get(slug='requisites')
    else:
        raise Http404
    context['page'] = page
    return render(request, 'page.html', context)


def delivery(request):
    context = {}
    if Page.objects.filter(slug='delivery').exists():
        page = Page.objects.get(slug='delivery')
    else:
        raise Http404
    context['page'] = page
    return render(request, 'page.html', context)


def payments(request):
    context = {}
    if Page.objects.filter(slug='payments').exists():
        page = Page.objects.get(slug='payments')
    else:
        raise Http404
    context['page'] = page
    return render(request, 'page.html', context)