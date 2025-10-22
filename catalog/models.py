from django.db import models

from loging.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=15,
        verbose_name="наименование категории",
        help_text="введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="введите описание",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=25,
        verbose_name="Название продукта",
        help_text="введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта", help_text="введите описание"
    )
    photo = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL, blank=True, null=True, related_name="product"
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    owner = models.ForeignKey(User, verbose_name='Продавец', help_text='Укажите продавца', blank=True, null=True, on_delete=models.SET_NULL)

    publish = models.BooleanField(default=False)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "category", "price"]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]

    def __str__(self):
        return self.name

