# Generated by Django 2.2.1 on 2019-05-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20190513_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookincart',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name='Количество'),
        ),
    ]
