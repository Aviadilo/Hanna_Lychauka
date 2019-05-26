# Generated by Django 2.2.1 on 2019-05-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0008_auto_20190406_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_type', models.CharField(max_length=30, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
    ]