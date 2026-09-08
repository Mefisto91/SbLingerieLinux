from django.urls import path

from .views.HomeView import HomeViewClass
from .views.CategoryView import CategoryViewClass
from .views.ProductView import ProductDetailView

app_name = "myDjangoApp"

urlpatterns = [
    # Home
    path("home/",HomeViewClass.as_view(),name="home"),
    # Categorías
    path("categoria/<slug:slug>/",CategoryViewClass.as_view(),name="categoria"),
    # Detalle de producto
    path("producto/<int:id>/",ProductDetailView.as_view(),name="producto_detalle"),
]