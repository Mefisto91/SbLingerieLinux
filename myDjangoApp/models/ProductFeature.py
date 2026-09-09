from django.db import models
from .ProductModel import Product


class ProductFeature(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="features"
    )

    name = models.CharField(
        max_length=100
    )

    value = models.CharField(
        max_length=255
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.product.name} - {self.name}"
