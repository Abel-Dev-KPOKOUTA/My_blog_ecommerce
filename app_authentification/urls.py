from django.contrib import admin
from django.urls import path , include 
from .import views

app_name="authentification"
urlpatterns = [
    path('connexion/' ,views.login_user , name="user_connexion"),
    path('inscription/' , views.register_user , name="user_inscription"),
    path('deconnexion/' , views.logout_user , name="user_deconnexion"),
]
