from django.views import View
from django.shortcuts import render
from django.db.models import Prefetch

from ..models.CategoryModel import Category
from ..models.ProductModel import Product
from ..models.ProductImage import ProductImage


class HomeViewClass(View):

    def get(self, request):

        imagenes_principales = ProductImage.objects.filter(
            is_primary=True
        )

        categorias = Category.objects.prefetch_related(
            Prefetch(
                "products",
                queryset=Product.objects.prefetch_related(
                    Prefetch(
                        "images",
                        queryset=imagenes_principales,
                        to_attr="imagenes_principales"
                    )
                ),
                to_attr="productos"
            )
        )

        productos_destacados = Product.objects.prefetch_related(
            Prefetch(
                "images",
                queryset=imagenes_principales,
                to_attr="imagenes_principales"
            )
        )[:6]

        return render(
            request,
            "index.html",
            {
                "categorias": categorias,
                "productos_destacados": productos_destacados,
            }
        )
