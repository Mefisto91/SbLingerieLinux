from django.views import View
from django.shortcuts import render, get_object_or_404

from ..models.ProductModel import Product

class ProductDetailView(View):
    def get(self, request, id):

        producto = get_object_or_404(
            Product.objects.prefetch_related("images"),
            id=id
        )

        return render(
            request,
            "productos/detalle.html",
            {
                "producto": producto,
            }
        )