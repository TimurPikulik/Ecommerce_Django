from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Product


# Create your views here.
def catalog(request, category_slug):
    if category_slug == "all":
        product_list = Product.objects.all().order_by('name')
    else:
        product_list = get_list_or_404(Product, category__slug=category_slug)

    paginator = Paginator(product_list, 1)
    page = request.GET.get('page', 1)
    page_range = paginator.get_elided_page_range(page, on_each_side=2, on_ends=1)
    try:
        goods = paginator.page(page)
    except PageNotAnInteger:
        goods = paginator.page(1)
    except EmptyPage:
        goods = paginator.page(paginator.num_pages)

    return render(request, "goods/catalog.html", context={
        "page": page,
        "goods": goods,
        "page_range": page_range,
    })


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "goods/product.html", context={
        "product": product
    })
