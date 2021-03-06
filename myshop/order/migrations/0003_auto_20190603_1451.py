# Generated by Django 2.2.1 on 2019-06-03 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190522_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='canceled',
            field=models.BooleanField(default=False, verbose_name='Отменен'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_cart', to='cart.Cart'),
        ),
    ]
