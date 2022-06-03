from django import template
from apps.catalog.views import get_current_order
from django.conf import settings


register = template.Library()


@register.inclusion_tag('parts/cart_popup.html')
def cart_popup(request):
    context = {}
    order = get_current_order(request)
    context['order'] = order
    context['MEDIA_URL'] = settings.MEDIA_URL
    return context
