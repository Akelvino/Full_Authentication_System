from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('', views.home, name='home'),
    path('welcome/', views.welcome_page, name='welcome_page'),
    path('register/', views.RegisterView, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'core/email.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'core/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]