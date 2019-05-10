from reference.models import *
from books.models import *


# функции, которые создают объекты справочников
def create_author(f_name, l_name, c):
    obj = Author(first_name=f_name, last_name=l_name, country=c)
    obj.save()
    print('В справочнике "Авторы" был создан объект {} с ключом={}'.format(obj.first_name, obj.pk))


def create_genre(n):
    obj = Genre(name=n)
    obj.save()
    print('В справочнике "Жанры" был создан объект {} с ключом={}'.format(obj.name, obj.pk))


def create_serie(n, d):
    obj = Series(name=n, description=d)
    obj.save()
    print('В справочнике "Серии" был создан объект {} с ключом={}'.format(obj.name, obj.pk))


def create_publish(n, c, ct):
    obj = Publish(name=n, country=c, city=ct)
    obj.save()
    print('В справочнике "Издательства" был создан объект {} с ключом={}'.format(obj.name, obj.pk))


def create_binding(type):
    obj = Binding(binding_type=type)
    obj.save()
    print('В справочнике "Переплеты" был создан объект {} с ключом={}'.format(obj.binding_type, obj.pk))


def create_format(sz):
    obj = BookFormat(size=sz)
    obj.save()
    print('В справочнике "Форматы" был создан объект {} с ключом={}'.format(obj.size, obj.pk))


# удаляет определенный объект из какого-либо справочника
def delete_object(ref_name, prim_key):
    ref_name.objects.get(pk=prim_key).delete()
    print('Из справочника {} был удален объект с ключом={}'.format(ref_name, prim_key))


# наполняет справочник большим количеством объектов
def create_set(amount):
    a_list = []
    for i in range(1, (amount + 1)):
        obj = Genre(name='Genre {}'.format(i))
        a_list.append(obj)
    Genre.objects.bulk_create(a_list)
    print('Было создано {} новых объектов в таблице "Жанры"'.format(amount))


# считает количество объектов в таблице
def count_von_count(table_name):
    x = table_name.objects.count()
    print("Количество объектов в таблице {} - {}".format(table_name, x))


# ищет количество авторов по кусочку фамилии
def count_by_name(part_name):
    x = Author.objects.filter(first_name__icontains=part_name).count()
    print('Количество авторов, фамилия которых содержит "{}" - {}'.format(part_name, x))


# создает объект или обновляет, если уже объект создан
def update_create(f_name, l_name, cntr):
    obj, created = Author.objects.update_or_create(
        first_name=f_name,
        last_name=l_name,
        defaults={'country': cntr}
    )


# выводит все книги, связанные с полем в справочнике
def list_of(ref_name, pr_key):
    obj = ref_name.objects.get(pk=pr_key)
    for i in obj.books.all():
        print(i)

# создает книгу из словаря
def create_book(bk):
    obj = Book(name=bk['name'], price=bk['price'], year=bk['year'], page=bk['page'], isbn=bk['isbn'], weight=bk['weight'],
               age_limit=bk['age_limit'], book_amount=bk['amount'], available=bk['available'], rate=bk['rate'])
    obj.serie = Series.objects.get(name=bk['serie_name'])
    obj.bind = Binding.objects.get(binding_type=bk['type'])
    obj.book_format = BookFormat.objects.get(pk=bk['size_pk'])
    obj.publish = Publish.objects.get(name=bk['publish_name'])
    obj.save()
    aut = Author.objects.get(pk=bk['author_pk'])
    genr = Genre.objects.get(name=bk['genre_name'])
    obj.author.add(aut)
    obj.genre.add(genr)


# пример словаря, который можно забросить в функцию create_book
new_book = {'name': 'Еще книга', 'price': 10, 'year': 1920, 'page': 299, 'isbn': '230-9424-92', 'weight': 199,
            'age_limit': 12, 'amount': 5, 'available': True, 'rate': 9, 'serie_name': 'Классика', 'type': 'Тканевая',
            'size_pk': 11, 'publish_name': 'Эксмо', 'author_pk': 15, 'genre_name': 'Сказка'}
