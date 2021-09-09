
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import TemplateView

from .views import account_activate, registrationView, dashboard, edit_details, delete_user
from django.contrib.auth import views as auth_views

from .forms import PwdResetConfirmForm, PwdResetForm, UserLoginForm

urlpatterns = [

    path('register/', registrationView, name='register'),
    path('login/', auth_views.LoginView.as_view(form_class=UserLoginForm, template_name = 'accounts/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #activation email
    path('activate/<slug:uidb64>/<slug:token>', account_activate, name='activate'),

    #User dashboard
    path('dashboad/',dashboard, name='dashboard'),
    path('profile/edit/', edit_details, name='edit'),
    path('profile/delete_user/', delete_user, name='delete_user'),
    path('profile/delete_user/confirm/', TemplateView.as_view(template_name='accounts/user/delete_confirm.html'),
               name='delete_confirmation'),

    #Reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset/password_reset_form.html',
                success_url='password_reset_email_confirm', email_template_name='accounts/password_reset/password_reset_email.html', 
                form_class=PwdResetForm), name='pwdreset'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
                template_name='accounts/password_reset/password_reset_confirm.html', success_url='{% url "password_reset_complete" %}',
                form_class=PwdResetConfirmForm), name='password_reset_confirm'),
    path('password_reset/password_reset_email_confirm/',
         TemplateView.as_view(template_name="accounts/password_reset/reset_status.html"), name='password_reset_done'),
    path('password_reset_confirm/Mg/password_reset_complete/',
         TemplateView.as_view(template_name="accounts/password_reset/reset_status.html"), name='password_reset_complete'),
]

