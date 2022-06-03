from django.contrib import admin
from apps.orders.models import Order, OrderDetails


class OrderDetailsInLine(admin.TabularInline):
    model = OrderDetails
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['datetime', ]
    inlines = [OrderDetailsInLine, ]