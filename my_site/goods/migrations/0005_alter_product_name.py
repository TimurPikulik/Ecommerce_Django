# Generated by Django 4.2.7 on 2024-01-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Наименование'),
        ),
    ]