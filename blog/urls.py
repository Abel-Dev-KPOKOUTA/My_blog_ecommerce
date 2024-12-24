from django.contrib import admin
from django.urls import path ,include
from .import views
app_name="blog_site"
urlpatterns = [
    path("mon_site/accueil/" , views.afficher , name="afficher"),
    path("article/info/<int:id_article>/", views.afficher_info_article , name="article_info"),
    path('article/recherche/',views.search, name="rechercher"),
]