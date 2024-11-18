'''

from blog.models import Article
def run():
    for i in range(10,20):
        article=Article()
        article.title=" Article N °{}" 
        article.description=" Description de l'Article N° {}"
        article.image="http://default"
        article.save()
        
print("Opération Réussir ...")

'''