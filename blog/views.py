from django.shortcuts import render , redirect , get_object_or_404
from .models import Article , Category
from django.http import HttpRequest

def afficher(request):
    all_articles=Article.objects.all()
    context={"all_articles" : all_articles}
    return render(request , "blog/index.html",context)


def afficher_info_article(request , id_article):
    article=Article.objects.get(pk=id_article)
    article_en_relation=Article.objects.filter(categorie=article.categorie)
    # On Peut aussi faire : context={"article":article} --> Mais pour ne pas perdre de temps , je prefere mettre directement le dictionnaire context dans le render ...
    return render(request,"blog/article_info.html" , {"article":article , "article_en_relation":article_en_relation})

def search(request):
    query=request.GET['article'] # Recuperation de la recherche et affichage de la recherche ...
    liste_de_recherche=Article.objects.filter(title__contains=query)
    return render(request,"blog/search.html", {"liste_de_recherche":liste_de_recherche})


'''
article_en_relation est la liste qui contient tout les articles de la categorie de l'article sur lequel on a cliquer ...
C'est à dire que si je clique sur une article qui est de categorie "Agriculture" , toutes les articles ayant la même categorie s'afficheront à notre extrême droit ...

'''