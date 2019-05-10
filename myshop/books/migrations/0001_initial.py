# Generated by Django 2.1.7 on 2019-04-06 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference', '0008_auto_20190406_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год издания')),
                ('page', models.PositiveSmallIntegerField(max_length=4, verbose_name='Количество страниц')),
                ('available', models.BooleanField(default=True, verbose_name='Доступна для заказа')),
                ('rate', models.FloatField(default=0, verbose_name='Рейтинг')),
                ('created_day', models.DateTimeField(auto_now_add=True, verbose_name='Время заполнения карточки')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('author', models.ManyToManyField(related_name='books', to='reference.Author', verbose_name='Автор')),
                ('bind', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='reference.Binding', verbose_name='Переплет')),
                ('genre', models.ManyToManyField(blank=True, null=True, related_name='books', to='reference.Genre', verbose_name='Жанр')),
                ('serie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='books', to='reference.Series', verbose_name='Серия')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
    ]
