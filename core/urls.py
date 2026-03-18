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
    path('logout/', LogoutView.as_view(), name='logout')
]