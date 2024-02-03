from django.contrib import admin

from .models import Cart


# Register your models here.

class CartTabularInline(admin.TabularInline):
    model = Cart
    fields = ("product", "quantity", "created_timestamp",)
    search_fields = ("product", "quantity", "created_timestamp",)
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user_display", "product", "quantity", "created_timestamp"]
    list_editable = ["quantity", ]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"
