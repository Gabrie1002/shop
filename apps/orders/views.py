from django.shortcuts import render, redirect
from apps.catalog.views import get_current_order
from apps.orders.forms import OrderForm
from apps.orders.models import Status
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User


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
            html = render_to_string('email/email.html', {'order': order})
            if not settings.DEBUG:
                send_mail('msg', html, settings.DEFAULT_FROM_EMAIL, get_managers_emails())
            else:
                print(html)
    context['form'] = OrderForm(instance=order)
    return render(request, 'orders/checkout.html', context)


def get_managers_emails():
    emails = []
    users = User.objects.filter(groups__name='managers')
    for user in users:
        if user.email:
            emails.append(user.email)
    return emails
