from django.shortcuts import render
# noinspection PyUnresolvedReferences
from goods.models import Category


# Create your views here.

def index(request):

    context = {
        "title": "Деревяшечка - Главная",
        "content": "Магазин мебели \"Деревяшечка\"",
    }

    return render(request, "main/index.html", context=context)


def about(request):
    return render(request, "main/about.html", context={
        "title": "Деревяшечка - О нас",
        "content": "О нас",
        "text": "Информация о интернет магазине"
    })
