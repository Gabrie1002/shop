from django import forms
from apps.orders.models import Order


class OrderForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    country = forms.CharField(required=True)
    city = forms.CharField(required=True)
    address = forms.CharField(required=True)
    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'country', 'city', 'address')
