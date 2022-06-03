from django.shortcuts import render, redirect
from apps.catalog.views import get_current_order
from apps.orders.forms import OrderForm
from apps.orders.models import Status


def cart(request):
    context = {}
    order = get_current_order(request)
    context['order'] = order
    return render(request, 'orders/cart.html', context)


def delete_product(request, pk):
    context = {}
    order = get_current_order(request)
    context['order'] = order
    if order.details.filter(pk=pk).exists():
        order.details.filter(pk=pk).delete()
    return redirect('/cart/')


def checkout(request):
    context = {}
    order = get_current_order(request)
    context['order'] = order

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()

            order.status = Status.objects.get(slug='waiting')
            order.save()

            context['result'] = True

    context['form'] = OrderForm(instance=order)
    return render(request, 'orders/checkout.html', context)