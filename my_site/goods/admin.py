from django.contrib import admin
from .models import Category, Product


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("name", "quantity", "price", "category",)


admin.site.site_header = "Панель администрирования"
admin.site.site_title = "Your Admin Portal"
admin.site.index_title = "Администрирование сайта"
