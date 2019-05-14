# Generated by Django 2.2.1 on 2019-05-11 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20190411_2322'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.CreateModel(
            name='BookInCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('created_day', models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения в корзину')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book', verbose_name='Товар')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_in_cart', to='cart.Cart', verbose_name='Корзина')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'unique_together': {('cart', 'book')},
            },
        ),
    ]
