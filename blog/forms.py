from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta :
        model=Article
        fields=['title','categorie','description','image']
        labels={'title':'Titre' , 'categorie':'Categorie' , 'description':'Description'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'categorie':forms.Select(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':5})
        }