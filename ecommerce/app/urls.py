from django.urls import path

from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home),
    path('category/', views.CategoryView.as_view(), name="category"),  # URL pattern for /category/
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),  # URL pattern for /category/<val>/
    path('brand/',views.BrandView.as_view(),name="brand"),
    path('brand/<val>',views.BrandView.as_view(),name="brand"),
    path('details/>',views.DetailView.as_view(),name="details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
