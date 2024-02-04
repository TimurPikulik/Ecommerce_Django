from django import forms
from django.contrib import admin

from .models import OrderItem, Order


# Register your models here.
class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem
    fields = ("product", 'name', "quantity", "price",)
    search_fields = ("product", 'name',)
    readonly_fields = ("created_timestamp",)
    extra = 0


class OrderTabularInline(admin.TabularInline):
    model = Order
    fields = ("requires_delivery", "status", 'payment_on_get', "is_paid", "created_timestamp",)
    search_fields = ("requires_delivery", 'payment_on_get', "is_paid", "created_timestamp",)
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "name", "quantity", "price",)
    search_fields = ("order", "product", 'name',)


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "requires_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "total_price",
        "created_timestamp",)
    search_fields = ("id",)
    readonly_fields = ("created_timestamp", "total_price",)

    inlines = [OrderItemTabularInline, ]

    @admin.display(description="Сумма заказа")
    def total_price(self, obj):
        return obj.total_price()
