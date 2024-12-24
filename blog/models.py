from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy
class Category(models.Model):
    name=models.CharField(max_length=120)
    def __str__(self):
        return self.name
    

class Article(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=50)
    categorie=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField()
    image=models.ImageField(null=True ,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

# categorie=models.ForeignKey(Category , on_delete=models.CASCADE) ==> Veut dire que si on supprime une categoriedonné tout les articles de cette categorie seront également supprimé ...
     
class Commentaire(models.Model):
    article_commenter=models.ForeignKey(Article , on_delete=models.CASCADE , null=True)
    commentaire=models.CharField(max_length=500, blank=True)

