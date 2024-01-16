from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        "title": "Test page",
        "content": "Zdarova",
        "list": ["dsfsdf", "sdfsdf",],
        "dict": {"sdsd": 1, },
        "is_auth": False
    }

    return render(request, "main/index.html", context=context)


def about(request):
    return HttpResponse("About")
