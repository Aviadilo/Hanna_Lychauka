# Generated by Django 2.2.1 on 2019-05-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_address',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_building',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Дом'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_city',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_flat',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Квартира'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_street',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица'),
        ),
    ]
