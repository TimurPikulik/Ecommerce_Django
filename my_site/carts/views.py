from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import Cart
from goods.models import Product
from carts.utils import get_user_cart


# Create your views here.

def cart_add(request):
    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    # return redirect(request.META.get('HTTP_REFERER'))
    user_cart = get_user_cart(request)
    cart_items_html = render_to_string(
        "carts/includes/includedcart.html",
        context={
            "carts": user_cart
        },
        request=request
    )
    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html
    }
    return JsonResponse(response_data)

def cart_change(request, product_slug):
    pass


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META.get('HTTP_REFERER'))
