from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

################# FORMUALIRE POUR LA CONNEXION D'UN UTILISATEUR ####################
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.error_messages["invalid_login"]='Identifiants ou mot de passe incorrects , merci veillez reessayer'

################ FORMULAIRE POUR L'INSCRIPTION D'UN UTILISATEUR ####################
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmer le mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        help_texts={'username':'' ,
                    'password1':'',
                    'password2':'',}
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.error_messages["password_mismatch"]="Les mots de passe ne correspondent pas ..."
        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None

