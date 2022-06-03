from django.contrib import admin
from apps.orders.models import Order, OrderDetails, Status


class OrderDetailsInLine(admin.TabularInline):
    model = OrderDetails
    extra = 0
    fields =['product', 'count', 'price', 'color', 'size', 'get_total', ]
    readonly_fields = ['get_total']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'get_total', 'status', ]
    inlines = [OrderDetailsInLine, ]


admin.site.register(Status)
