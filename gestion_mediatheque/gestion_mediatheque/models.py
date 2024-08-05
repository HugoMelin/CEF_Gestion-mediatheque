from django.db import models
from django.contrib.auth.models import AbstractUser


class Media (models.Model):
    nom = models.fields.CharField(max_length=150)
    dateEmprunt = models.fields.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    idEmprunteur = models.ForeignKey("Membre", on_delete=models.SET_NULL, blank=True, null=True)
    disponible = models.fields.BooleanField(default=True)

    @classmethod
    def create(cls, nom):
        newMedia = cls(nom=nom)
        newMedia.save()
        return newMedia


class Livre (Media):
    auteur = models.fields.CharField(max_length=150)

    @classmethod
    def create(cls, nom, auteur):
        newLivre = cls(nom=nom, auteur=auteur)
        newLivre.save()
        return newLivre


class CD (Media):
    artiste = models.fields.CharField(max_length=150)

    @classmethod
    def create(cls, nom, artiste):
        newCD = cls(nom=nom, artiste=artiste)
        newCD.save()
        return newCD


class DVD (Media):
    realisateur = models.fields.CharField(max_length=150)

    @classmethod
    def create(cls, nom, realisateur):
        newDVD = cls(nom=nom, realisateur=realisateur)
        newDVD.save()
        return newDVD


class JeuxPlateaux (models.Model):
    nom = models.fields.CharField(max_length=150)
    createur = models.fields.CharField(max_length=150)

    @classmethod
    def create(cls, nom, createur):
        newJeuxPlateaux = cls(nom=nom, createur=createur)
        newJeuxPlateaux.save()
        return newJeuxPlateaux


class Membre (models.Model):
    nom = models.fields.CharField(max_length=150)
    nbEmprunt = models.fields.IntegerField(default=0)
    bloque = models.fields.BooleanField(default=False)

    @classmethod
    def create(cls, nom):
        newMembre = cls(nom=nom)
        newMembre.save()
        return newMembre


class Bibliothequaire (AbstractUser):
    email = models.fields.CharField(max_length=150, default="")

    @classmethod
    def create(cls, username, password, email=""):
        Bibliothequaire.objects.create_user(username, email, password)
