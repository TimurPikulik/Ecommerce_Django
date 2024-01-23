from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Product


# Create your views here.
def catalog(request, category_slug):
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug == "all":
        product_list = Product.objects.all().order_by('name')
    else:
        product_list = get_list_or_404(Product, category__slug=category_slug)
    if on_sale:
        product_list = product_list.filter(discount__gt=0)
    if order_by and order_by != 'default':
        product_list = product_list.order_by(order_by)

    paginator = Paginator(product_list, 4)
    page = request.GET.get('page', 1)
    try:
        goods = paginator.page(page)
        page_range = paginator.get_elided_page_range(page, on_each_side=2, on_ends=1)
    except PageNotAnInteger:
        goods = paginator.page(1)
        page_range = paginator.get_elided_page_range(1, on_each_side=2, on_ends=1)
    except EmptyPage:
        goods = paginator.page(paginator.num_pages)
        page_range = paginator.get_elided_page_range(paginator.num_pages, on_each_side=2, on_ends=1)

    return render(request, "goods/catalog.html", context={
        "page": page,
        "goods": goods,
        "page_range": page_range,
        "slug": category_slug,
    })


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "goods/product.html", context={
        "product": product
    })
