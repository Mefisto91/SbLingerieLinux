from django.urls import path
from .views.HomeView import HomeViewClass
from .views.CategoryView import CategoryViewClass

app_name="myDjangoApp"

urlpatterns = [
    path('home/', HomeViewClass.as_view(), name="home"),
    path("categoria/<slug:slug>/", CategoryViewClass.as_view(), name="categoria"),
]