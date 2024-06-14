from django.urls import path

from django.conf import settings

from .forms import LoginForm, MyPassworChangeForm, MySetPasswordForm,MyPasswordResetForm
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
    

    path('add-to-cart/<int:pk>',views.add_to_cart,name='add-to-cart'),
    path('cart/',views.show_cart,name='cart'),
    path('checkout/',views.checkout.as_view(),name='checkout'),
    path('pluscart/',views.plus_cart,name='pluscart' ),
    path('minuscart/',views.minus_cart,name='minuscart' ),
    path('removecart/',views.remove_cart,name='removecart' ),

    #login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form = LoginForm), name='login'),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MyPassworChangeForm, success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('logout/',auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password-reset/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done', auth_view.PasswordResetDoneView.as_view(template_name='app/password-reset/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/password-reset/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/password-reset/password_reset_complete.html'),name='password_reset_complete'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
