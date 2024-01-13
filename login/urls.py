from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='web-home'),
    path('sign/', views.store_users, name='user-submit'),
    path('login/', views.login, name='web-home'),
    path('log/', views.login_user, name='user-login')
]
