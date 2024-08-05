from django import forms

class ConnexionUser(forms.Form):
    name = forms.CharField(label="Non", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), label="Mot de passe", required=True)


class AddLivre(forms.Form):
    nom = forms.CharField(label="Non", required=True)
    auteur = forms.CharField(label="Auteur", required=True)
