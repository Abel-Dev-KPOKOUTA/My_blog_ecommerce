from django.contrib import admin
from django.urls import path , include
from .import views


app_name="app_admin"

urlpatterns = [
    path('tableau/',views.tableau_bord , name='tableau'),
    path('user_articles/',views.user_articles , name="mes_articles"),
    path('ajouter_user_article/',views.AddUserArticles.as_view() , name="Add_articles"),
    path('update_article/<int:pk>/',views.UpdateArticle.as_view() , name="update_article"),
    path('delete_article/<int:pk>/',views.DeleteArticle.as_view() , name="delete_article"),
    path('delete_article/error/permission_autorisation/',views.permission_return , name="permission"),
]

