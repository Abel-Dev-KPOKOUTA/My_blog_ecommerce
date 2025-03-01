from django.shortcuts import render, redirect , get_object_or_404
from blog.models import Article
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import ArticleForm
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

def tableau_bord(request):
    # Nombre totales d'utilisateurs 
    users_count=User.objects.count()
    # Nombre totales d'articles 
    totals_produits=Article.objects.count()
    # Nombres de ventes 
    totals_ventes=0
    # Nombres de commandes 
    totals_commandes=0
    context={"users_count":users_count,"totals_produits":totals_produits,"totals_ventes":totals_ventes,"totals_commandes":totals_commandes}

    return render(request, "app_admin/index.html" ,context)

@login_required
def user_articles(request):
    has_perm = request.user.has_perm("blog.delete_article")
    mes_articles_user = Article.objects.filter(user=request.user)
    return render(request, "app_admin/mes_articles.html", {"mes_articles_user":mes_articles_user, "has_perm":has_perm})

class AddUserArticles(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app_admin/ajouter_add.html'
    success_url = reverse_lazy('app_admin:mes_articles')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateArticle(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'app_admin/modifier_edit.html'
    success_url = reverse_lazy('app_admin:mes_articles')

def permission_return(request):
    return render(request, "app_admin/403.html")

class DeleteArticle(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    template_name = 'app_admin/supprimer_remove.html'
    success_url = reverse_lazy('app_admin:mes_articles')
    permission_required = 'blog.delete_article'

    def handle_no_permission(self):
        return redirect('app_admin:permission')
