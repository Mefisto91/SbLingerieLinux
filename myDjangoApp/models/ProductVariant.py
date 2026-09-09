from django.db import models
from .ProductModel import Product


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants"
    )

    color = models.CharField(
        max_length=50
    )

    size = models.CharField(
        max_length=20
    )

    available_quantity = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["id"]

        constraints = [
            models.UniqueConstraint(
                fields=["product", "color", "size"],
                name="unique_product_variant"
            )
        ]

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"