from django.db import models


class Blog(models.Model):
    heading = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        help_text="Введите название заголовок",
    )
    content = models.TextField(
        verbose_name="Содержимое",
        help_text="Введите содержимое",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="blog/photo/",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )

    created_at = models.DateField(auto_now_add=True)

    publication_at = models.BooleanField(default=True)

    view_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блог"
        ordering = [
            "heading",
        ]

    def __str__(self):
        return self.heading
