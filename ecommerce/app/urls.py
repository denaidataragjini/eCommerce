from django.urls import path

from django.conf import settings

from .forms import LoginForm, MyPassworChangeForm,PasswordResetForm
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
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),
    
    #login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form = LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=PasswordResetForm),name='password_reset'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPassworChangeForm, success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
