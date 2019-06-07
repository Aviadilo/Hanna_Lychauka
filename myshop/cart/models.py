from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        related_name='cart_of_user',
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    created_day = models.DateTimeField(
        "Дата внесения в корзину",
        auto_now=False,
        auto_now_add=True)

    updated_date = models.DateTimeField(
        "Дата последнего изменения",
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return "Корзина {} покупателя {}".format(self.pk, self.user)

    @property
    def books_in_cart_count(self):
        total = 0
        for product in self.user_cart.all():
            total += product.quantity
        return total

    @property
    def total_cart_price(self):
        total = 0
        for product in self.user_cart.all():
            total += product.price_total
        return total

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина', related_name='user_cart')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Товар', related_name='book_in_cart')
    quantity = models.PositiveIntegerField("Количество")

    created_day = models.DateTimeField(
        "Дата внесения в корзину",
        auto_now=False,
        auto_now_add=True)

    updated_date = models.DateTimeField(
        "Дата последнего изменения",
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return self.book.name

    @property
    def price_total(self):
        return self.book.price * self.quantity

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        unique_together = [['cart', 'book']]
