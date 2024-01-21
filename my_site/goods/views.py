from django.shortcuts import render

from .models import Product


# Create your views here.

def catalog(request):
    goods = Product.objects.all()
    return render(request, "goods/catalog.html", context={
        "goods": goods,
    })


def product(request):
    return render(request, "goods/product.html", context={

    })
