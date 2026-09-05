from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from ..models.CategoryModel import Category


class CategoryViewClass(ListView):
    template_name = "categoria.html"
    context_object_name = "productos"

    def get_queryset(self):
        categoria = get_object_or_404(
            Category,
            slug=self.kwargs["slug"]
        )

        return categoria.products.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categoria"] = get_object_or_404(
            Category,
            slug=self.kwargs["slug"]
        )

        return context
