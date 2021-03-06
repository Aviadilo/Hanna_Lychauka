# Generated by Django 2.2 on 2019-04-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0002_auto_20190404_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=50, null=True, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
    ]
