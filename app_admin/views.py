from django.shortcuts import render , redirect
from blog.models import Article 
from django.views.generic.edit import UpdateView , CreateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import ArticleForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


def tableau_bord(request):
    return render(request,"app_admin/index.html")


@login_required
def user_articles(request):
    has_perm=False
    if request.user.has_perm("Blog.delete_article"):
        has_perm=True
    else : 
        has_perm=False

    mes_articles_user=Article.objects.filter(user=request.user)
    return render(request,"app_admin/mes_articles.html",{"mes_articles_user":mes_articles_user,"has_perm":has_perm})


class AddUserArticles(LoginRequiredMixin , CreateView):
    model=Article
    form_class=ArticleForm
    template_name='app_admin/ajouter_add.html'
    success_url=reverse_lazy('app_admin:mes_articles') #Pour vers la redirection dans ce cas , il faut import reverse_laey de django.urls et le mettre devant success_url

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form) 
    

class UpdateArticle(LoginRequiredMixin , UpdateView):
    model=Article
    form_class=ArticleForm
    template_name='app_admin/modifier_edit.html'
    success_url=reverse_lazy('app_admin:mes_articles')

def permission_return(request):
    return render(request,"app_admin/403.html")

class DeleteArticle(LoginRequiredMixin , DeleteView):
    model=Article
    template_name='app_admin/supprimer_remove.html'
    success_url=reverse_lazy('app_admin:mes_articles')
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm("blog.delete_article"):
            return redirect('app_admin:permission')

        return super().dispatch(request, *args, **kwargs)
    

