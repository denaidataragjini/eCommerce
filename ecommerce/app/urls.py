from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('category/',views.CategoryView.as_view(),name="category"),
    path('brand/',views.BrandView.as_view(),name="brand"),
]
