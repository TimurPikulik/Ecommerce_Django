from django.db import models
from django.db.models import UniqueConstraint
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категории'
        db_table = 'category'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание продукта')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=3, decimal_places=2, verbose_name='Скидка')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name='products',
                                 verbose_name='Категория')

    class Meta:
        verbose_name = 'Продукт'
        db_table = 'product'
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

