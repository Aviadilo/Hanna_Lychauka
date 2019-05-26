from django.db import models

class Book(models.Model):
    name = models.CharField(
        "Название",
        null=False,
        blank=False,
        max_length=200)

    image = models.ImageField(
        "Обложка",
        upload_to='book_images/',
        null=True,
        blank=True)

    # можно выбрать несколько авторов
    author = models.ManyToManyField(
        "reference.Author",
        related_name="books",
        verbose_name="Автор")

    price = models.DecimalField(
        "Цена",
        max_digits=5,
        decimal_places=2)  # decimal_places - количество нулей после запятой

    # можно выбрать одну серию
    serie = models.ForeignKey(
        "reference.Series",
        related_name="books",
        verbose_name="Серия",
        null=True,
        blank=True,
        on_delete=models.PROTECT)

    # можно выбрать несколько жанров
    genre = models.ManyToManyField(
        "reference.Genre",
        related_name="books",
        blank=True,
        verbose_name="Жанр")

    year = models.PositiveSmallIntegerField(
        "Год издания",
        null=True,
        blank=True)

    page = models.PositiveSmallIntegerField(
        "Количество страниц",
        null=True,
        blank=True)

    bind = models.ForeignKey(
        "reference.Binding",
        related_name="books",
        verbose_name="Переплет",
        null=True,
        blank=True,
        on_delete=models.PROTECT)

    book_format = models.ForeignKey(
        "reference.BookFormat",
        related_name="books",
        verbose_name="Формат",
        null=True,
        blank=True,
        on_delete=models.PROTECT)

    isbn = models.CharField(
        "ISBN",
        default="0",
        unique=True,
        max_length=20)

    weight = models.PositiveSmallIntegerField(
        "Вес, гр",
        null=True,
        blank=True, )

    age_limit = models.PositiveSmallIntegerField(
        "Возрастные ограничения",
        null=True,
        blank=True,)

    publish = models.ForeignKey(
        "reference.Publish",
        related_name="books",
        verbose_name="Издательство",
        null=True,
        blank=True,
        on_delete=models.PROTECT)

    book_amount = models.PositiveIntegerField(
        "Кол-во книг в наличии",
        default=0)

    available = models.BooleanField(
        "Доступна для заказа",
        default=True)

    rate = models.FloatField(
        "Рейтинг",
        default=0)

    created_day = models.DateTimeField(
        "Дата внесения в каталог",
        auto_now=False,
        auto_now_add=True)

    updated_date = models.DateTimeField(
        "Дата последнего изменения",
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        permissions = [('edit_content', 'content manager'), ('edit_order', 'order manager'), ('market', 'for marketers')]
