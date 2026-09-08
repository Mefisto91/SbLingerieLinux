from django.db import models
from .ProductModel import Product

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="productos/"
    )

    is_primary = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"Imagen de {self.product.name}"