from django.urls import path
from . import views

urlpatterns = [
    path('',views.drinks,name='web-drinks')
]