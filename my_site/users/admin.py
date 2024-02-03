from django.contrib import admin
from .models import User
from carts.admin import CartTabularInline


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", ]
    search_fields = ["username", "first_name", "last_name", ]

    inlines = [CartTabularInline,]
