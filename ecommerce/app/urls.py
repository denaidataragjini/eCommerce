from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('category/', views.CategoryView.as_view(), name="category"),  # URL pattern for /category/
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),  # URL pattern for /category/<val>/
    path('brand/',views.BrandView.as_view(),name="brand"),
    path('brand/<val>',views.BrandView.as_view(),name="brand"),
]
