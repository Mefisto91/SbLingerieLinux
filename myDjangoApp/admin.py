from django.contrib import admin

from .models.CategoryModel import Category
from .models.ProductModel import Product
from .models.ProductImage import ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "name",
        "description",
    )

    inlines = [
        ProductImageInline,
    ]
