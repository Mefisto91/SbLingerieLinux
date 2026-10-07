from django.urls import path
from django.shortcuts import redirect

from .views.HomeView import HomeViewClass
from .views.CategoryView import CategoryViewClass
from .views.ProductView import ProductDetailView

app_name = "myDjangoApp"

urlpatterns = [
    # Redirección de la raíz al Home
    path("", lambda request: redirect("myDjangoApp:home")),

    # Home
    path("home/", HomeViewClass.as_view(), name="home"),

    # Categorías
    path("categoria/<slug:slug>/", CategoryViewClass.as_view(), name="categoria"),

    # Detalle de producto
    path("producto/<int:id>/", ProductDetailView.as_view(), name="producto_detalle"),
]