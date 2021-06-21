from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.home, name ='home'),
path('signUp/', views.signUp, name ='signUp'),
path('signUpView/', views.signUpView, name ='signUpView'),
path('login/', views.Login, name="login"),
path('loginView/', views.loginView, name ='loginView'),
path('logout/', views.logoutView, name='logout'),
path('addStudent/', views.addStudent, name='addStudent'),
]
