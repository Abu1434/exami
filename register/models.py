from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    pass


class ProductModel(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=255, null=True, blank=True)
    price = models.PositiveIntegerField()
    created_at = models.DateField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
