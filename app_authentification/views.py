from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import authenticate , login , logout 
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm , CustomAuthenticationForm

def login_user(request):
    if request.method=="POST":
        formulaire=CustomAuthenticationForm(request , data=request.POST)
        if formulaire.is_valid():
            username=formulaire.cleaned_data.get("username")
            password=formulaire.cleaned_data.get("password")
            user=authenticate(request , username=username , password=password)
            if user is not None :
                login(request,user)
                return redirect("app_admin:tableau")
        else :
            messages.info(request,"Nom d'utilisateur ou mot de passe incorrect ...")
    else:
        formulaire=CustomAuthenticationForm() # AuthentificationForm() est un formualaire possedant deux champs : une pour le username et l'autre pour le mot de passe
    return render(request,"app_authentification/page_connexion.html",{"formulaire":formulaire})


def logout_user(request):
    logout(request)
    return redirect('blog_site:afficher')


def register_user(request):
    if request.method=='POST':
       formulaire=CustomUserCreationForm(request.POST)
       if formulaire.is_valid():
           formulaire.save()
           return redirect("blog_site:afficher")
    else:
        formulaire=CustomUserCreationForm()
    return render(request,"app_authentification/page_inscription.html",{"formulaire":formulaire})



