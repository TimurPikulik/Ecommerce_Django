from django.db import models
from users.models import User

from goods.models import Product


# Create your models here.

class CartQuerySet(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, blank=True, null=True, verbose_name='Ключ сессии')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = "cart"
        verbose_name = 'Корзины'
        verbose_name_plural = 'Корзина'
        ordering = ['id', ]

    objects = CartQuerySet().as_manager()

    def __str__(self):
        if self.user:
            return f"Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"

        return f"Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}"

    def products_price(self):
        return round(self.product.get_discount_price() * self.quantity, 2)
