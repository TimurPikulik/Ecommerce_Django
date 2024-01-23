from goods.models import Product
from django.db.models import Q


def q_search(querry):
    if querry.isnumeric() and len(querry) <= 5:
        return Product.objects.filter(id=int(querry))

    keywords = [word for word in querry.split() if len(word) > 2]
    q_obj = Q()

    for token in keywords:
        q_obj |= Q(description__icontains=token)
        q_obj |= Q(name__icontains=token)

    return Product.objects.filter(q_obj)
