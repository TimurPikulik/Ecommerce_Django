from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from goods.models import Product
from django.db.models import Q


def q_search(query):
    if query.isnumeric() and len(query) <= 5:
        return Product.objects.filter(id=int(query))
    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    result = Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    result = result.annotate(
        nameline=SearchHeadline(
            "name",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>')
    )
    result = result.annotate(
        descriptionline=SearchHeadline(
            "description",
            query,
            start_sel='<span style="background-color: yellow;">',
            stop_sel='</span>')
    )

    return result
    # keywords = [word for word in querry.split() if len(word) > 2]
    # q_obj = Q()
    #
    # for token in keywords:
    #     q_obj |= Q(description__icontains=token)
    #     q_obj |= Q(name__icontains=token)
    #
    # return Product.objects.filter(q_obj)
