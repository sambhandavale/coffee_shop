from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.user_profile, name='view_profile'),
    path('', views.view_profile, name='default_profile'),
]

