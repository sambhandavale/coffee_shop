from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_to_default_profile, name='redirect_to_default_profile'),
    path('<str:username>/', views.user_profile, name='view_profile'),
]

