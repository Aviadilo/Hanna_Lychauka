from django.db import models
from cart.models import User


class CommentToBook(models.Model):
    commented_book = models.ForeignKey(
        "books.Book",
        related_name="commented_book",
        verbose_name="Книга с комментарием",
        on_delete=models.CASCADE
    )

    comment_to_book = models.TextField(
        "Комментарий к книге"
    )

    commented_user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    created_day = models.DateTimeField(
        "Дата создания комментария",
        auto_now=False,
        auto_now_add=True)

    def __str__(self):
        return "Коммент пользователя {} о книге {}".format(self.commented_user, self.commented_book)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
