from django.views import View
from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch

from ..models.CategoryModel import Category
from ..models.ProductModel import Product
from ..models.ProductImage import ProductImage

class CategoryViewClass(View):
    def get(self, request, slug):

        imagenes_principales = ProductImage.objects.filter(
            is_primary=True
        )

        categoria = get_object_or_404(
            Category,
            slug=slug
        )

        productos = Product.objects.filter(
            category=categoria
        ).prefetch_related(
            Prefetch(
                "images",
                queryset=imagenes_principales,
                to_attr="imagenes_principales"
            )
        )

        return render(
            request,
            "categoria.html",
            {
                "categoria": categoria,
                "productos": productos,
            }
        )