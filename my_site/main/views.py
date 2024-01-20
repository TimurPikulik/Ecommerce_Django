from django.shortcuts import render
# noinspection PyUnresolvedReferences
from goods.models import Category


# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {
        "title": "Деревяшечка - Главная",
        "content": "Магазин мебели \"Деревяшечка\"",
        "categories": categories
    }

    return render(request, "main/index.html", context=context)


def about(request):
    return render(request, "main/about.html", context={
        "title": "Деревяшечка - О нас",
        "content": "О нас",
        "text": "Информация о интернет магазине"
    })
