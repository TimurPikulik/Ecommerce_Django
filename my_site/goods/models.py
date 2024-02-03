from django.db import models
from django.urls import reverse
from django.utils.html import format_html


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
    image = models.ImageField(upload_to='goods', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT, related_name='products',
                                 verbose_name='Категория')

    class Meta:
        verbose_name = 'Продукт'
        db_table = 'product'
        verbose_name_plural = "Продукты"
        ordering = ('name',)

    def __str__(self):
        return self.name

    def image_preview(self):
        content = ""
        if self.image:
            content = format_html(f'<img src = "{self.image.url}" width = "100"/>')
        return content

    image_preview.short_description = 'Изображение'
    image_preview.allow_tags = True

    def get_id(self):
        return f"{self.id:05}"

    def get_discount_price(self):
        if self.discount:
            return round(self.price - (self.price * (self.discount / 100)),2)
        return self.price

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"slug": self.slug})
