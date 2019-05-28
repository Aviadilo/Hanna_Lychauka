from django.db import models

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

    created_day = models.DateTimeField(
        "Дата создания комментария",
        auto_now=False,
        auto_now_add=True)

    def __str__(self):
        return "Коммент"

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
