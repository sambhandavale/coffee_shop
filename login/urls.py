from django.urls import path
from . import views

urlpatterns = [
    # path('sign/', views.store_users, name='user-submit'),
    # path('log/', views.login_user, name='user-login'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.login, name='logout'),
]
