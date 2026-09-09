from django.db import models
from .CategoryModel import Category

class Product(models.Model):
    category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name="products"
    )

    reference = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=150
    )

    description = models.TextField(
        blank=True
    )

    material = models.CharField(
        max_length=100,
        blank=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.name

