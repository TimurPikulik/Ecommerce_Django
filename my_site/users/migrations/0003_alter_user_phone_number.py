# Generated by Django 4.2.7 on 2024-02-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Номер телефона'),
        ),
    ]
