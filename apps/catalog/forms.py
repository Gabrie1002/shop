from django import forms
from apps.orders.models import OrderDetails


class ProductForm(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ('count', 'color', 'size')
