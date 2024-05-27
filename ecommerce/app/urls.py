from django.urls import path

from django.conf import settings

from .forms import LoginForm,PasswordResetForm
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.home),
    path('category/', views.CategoryView.as_view(), name="category"),  # URL pattern for /category/
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),  # URL pattern for /category/<val>/
    path('brand/',views.BrandView.as_view(),name="brand"),
    path('brand/<val>',views.BrandView.as_view(),name="brand"),
    path('details/<int:pk>', views.DetailView.as_view(), name="details"),
    
    #login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form = LoginForm), name='login'),
    path('password-reset', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=PasswordResetForm),name='password_reset'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
