from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      "class": "form-control",
                                      "placeholder": "Введите имя пользователя"}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          "class": "form-control",
                                          "placeholder": "Введите пароль"}),
    )

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = {
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        }

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control",
    #                "placeholder": "Введите ваше имя"}
    #     )
    # )
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control",
    #                "placeholder": "Введите вашу фамилию"}
    #     )
    # )
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control",
    #                "placeholder": "Введите имя пользователя"}
    #     )
    # )
    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs={"class": "form-control",
    #                "placeholder": "Введите вашу почту"}
    #     )
    # )
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={"class": "form-control",
    #                "placeholder": "Введите ваш пароль"}
    #     )
    # )
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={"class": "form-control",
    #                "placeholder": "Подтвердите ваш пароль"}
    #     )
    # )