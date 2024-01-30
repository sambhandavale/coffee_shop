from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog-home'),
    path('add_review/', views.write_review, name='write_review'),
]
