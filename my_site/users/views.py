from django.shortcuts import render


# Create your views here.
def login(request):
    context = {
        "title": "Деревяшечка - Логин",
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        "title": "Деревяшечка - Регистрация",
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        "title": "Деревяшечка - Профиль",
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    context = {
        "title": "Деревяшечка - Выход",
    }
    return render(request, 'users/profile.html', context)
