# Generated by Django 2.2.1 on 2019-06-03 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20190524_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('edit_content', 'content manager'), ('edit_order', 'order manager'), ('market', 'for marketers')], 'verbose_name': 'Книга', 'verbose_name_plural': 'Книги'},
        ),
    ]
