from django.contrib import admin
from django.utils.html import format_html, mark_safe

from .models import Category, Product


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("name", "image_preview", "quantity", "price", "discount", "category",)
    readonly_fields = ["image_preview"]


admin.site.site_header = "Панель администрирования"
admin.site.site_title = "Your Admin Portal"
admin.site.index_title = "Администрирование сайта"
