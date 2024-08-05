from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from gestion_mediatheque.models import Media, Livre, CD, DVD, JeuxPlateaux, Membre
from gestion_mediatheque.forms import ConnexionUser, AddLivre
import datetime
import logging


logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y%H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def accueil(request):
    livres = Livre.objects.all()
    cds = CD.objects.all()
    dvds = DVD.objects.all()
    jeuxplateux = JeuxPlateaux.objects.all()
    logger.info("La page d'accueil a été chargée.")
    return render(request, 'accueil.html',
                  {'livres': livres,
                   'cds': cds,
                   'dvds': dvds,
                   'jeuxplateux': jeuxplateux})


def connexion(request):
    connexionForm = ConnexionUser()
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            logger.info("Utilisateur " + str(user) + " connecté")
            return redirect("bibliothequaire")
        else:
            logger.error("L'utilisateur n'a pas pus être connecté")
            return redirect("accueil")
    elif request.user.is_authenticated:
        return redirect("bibliothequaire")
    return render(request, 'connexion.html',
                  {'connexionForm': connexionForm})


@login_required
def bibliothequaire(request):
    membres = Membre.objects.all()
    livres = Livre.objects.all()
    cds = CD.objects.all()
    dvds = DVD.objects.all()
    jeuxplateaux = JeuxPlateaux.objects.all()
    logger.info("La page biliothequaire est chargé")
    return render(request, "bibliothequaire.html",
                  {'membres': membres,
                   'livres': livres,
                   'cds': cds,
                   'dvds': dvds,
                   'jeuxplateaux': jeuxplateaux})


def deconnexion(request):
    logout(request)
    logger.info("Utilisateur déconnecté")
    return redirect("accueil")


@login_required
def createMember(request):
    if request.method == 'POST':
        name = request.POST['newUserName']
        Membre.create(name)
        logger.info("Le membre : " + " a été créé")
        return redirect("bibliothequaire")
    return redirect("bibliothequaire")


@login_required
def supprimerMembre(request, id):
    membre = Membre.objects.get(pk=id)
    logger.info("Le membre " + str(membre.nom) + "a été supprimé.")
    membre.delete()
    return redirect("bibliothequaire")


@login_required
def update_member(request, id):
    membre = Membre.objects.get(pk=id)
    if request.method == 'POST':
        membre.nom = request.POST['nom']
        membre.nbEmprunt = int(request.POST['nbEmprunt'])
        if membre.nbEmprunt < 3:
            membre.bloque = False
        else:
            membre.bloque = True
        membre.save()
        logger.info("Le membre " + membre.nom + " a été modifié.")
        return redirect("bibliothequaire")
    else:
        return render(request,
                      'update_member.html',
                      {'membre': membre})


@login_required
def add_livre(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        auteur = request.POST['auteur']
        Livre.create(nom, auteur)
        logger.info("Le livre " + nom + " a été ajouté")
        return redirect("bibliothequaire")
    else:
        addlivre = AddLivre()
        return render(request, 'add_livre.html',
                      {'addlivre': addlivre})

@login_required
def supprimerLivre(request, id):
    livre = Livre.objects.get(pk=id)
    logger.info("Le livre " + livre.nom + " a été supprimé")
    livre.delete()
    return redirect("bibliothequaire")


@login_required
def updateLivre(request, id):
    livre = Livre.objects.get(pk=id)
    if request.method == 'POST':
        livre.nom = request.POST['nom']
        livre.auteur = request.POST['auteur']
        livre.save()
        logger.info("Le livre " + livre.nom + " a été modifié.")
        return redirect("bibliothequaire")
    else:
        return render(request,
                      'update_livre.html',
                      {'livre': livre})


@login_required
def add_cd(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        auteur = request.POST['auteur']
        CD.create(nom, auteur)
        logger.info("Le CD " + nom + " a été ajouté")
        return redirect("bibliothequaire")
    else:
        addlivre = AddLivre()
        return render(request, 'add_cd.html',
                      {'addcd': addlivre})


@login_required
def supprimerCD(request, id):
    cd = CD.objects.get(pk=id)
    logger.info("Le CD " + cd.nom + " a été supprimé")
    cd.delete()
    return redirect("bibliothequaire")


@login_required
def updateCD(request, id):
    cd = CD.objects.get(pk=id)
    if request.method == 'POST':
        cd.nom = request.POST['nom']
        cd.artiste = request.POST['artiste']
        cd.save()
        logger.info("Le CD " + cd.nom + " a été modifié.")
        return redirect("bibliothequaire")
    else:
        return render(request,
                      'update_cd.html',
                      {'cd': cd})


@login_required
def add_dvd(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        realisateur = request.POST['auteur']
        DVD.create(nom, realisateur)
        logger.info("Le DVD " + nom + " a été ajouté")
        return redirect("bibliothequaire")
    else:
        addlivre = AddLivre()
        return render(request, 'add_dvd.html',
                      {'adddvd': addlivre})


@login_required
def supprimerDvd(request, id):
    dvd = DVD.objects.get(pk=id)
    logger.info("Le DVD " + dvd.nom + " a été supprimé")
    dvd.delete()
    return redirect("bibliothequaire")


@login_required
def updateDvd(request, id):
    dvd = DVD.objects.get(pk=id)
    if request.method == 'POST':
        dvd.nom = request.POST['nom']
        dvd.realisateur = request.POST['realisateur']
        dvd.save()
        logger.info("Le DVD " + dvd.nom + " a été modifié.")
        return redirect("bibliothequaire")
    else:
        return render(request,
                      'update_dvd.html',
                      {'dvd': dvd})


@login_required
def add_jeuxplateux(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        realisateur = request.POST['auteur']
        JeuxPlateaux.create(nom, realisateur)
        logger.info("Le Jeux de Plateaux " + nom + " a été ajouté")
        return redirect("bibliothequaire")
    else:
        addlivre = AddLivre()
        return render(request, 'add_jeuxplateaux.html',
                      {'addjeuxplateaux': addlivre})


@login_required
def supprimerJeuxPlateaux(request, id):
    jeuxPlateaux = JeuxPlateaux.objects.get(pk=id)
    logger.info("Le jeux de plateaux " + jeuxPlateaux.nom + " a été supprimé")
    jeuxPlateaux.delete()
    return redirect("bibliothequaire")


@login_required
def updateJeuxPlateaux(request, id):
    jeuxPlateaux = JeuxPlateaux.objects.get(pk=id)
    if request.method == 'POST':
        jeuxPlateaux.nom = request.POST['nom']
        jeuxPlateaux.createur = request.POST['createur']
        jeuxPlateaux.save()
        logger.info("Le jeux de plateaux " + jeuxPlateaux.nom + " a été modifié.")
        return redirect("bibliothequaire")
    else:
        return render(request,
                      'update_jeuxPlateaux.html',
                      {'jeuxPlateaux': jeuxPlateaux})


@login_required
def emprunt(request, id):
    media = Media.objects.get(pk=id)
    if request.method == 'POST':
        emprunteur = Membre.objects.get(pk=request.POST['emprunteur'])
        if emprunteur.nbEmprunt < 3:
            media.idEmprunteur = emprunteur
            media.dateEmprunt = request.POST['date']
            media.disponible = False
            media.save()
            emprunteur.nbEmprunt += 1
            if emprunteur.nbEmprunt >= 3:
                emprunteur.bloque = True
            emprunteur.save()
            logger.info(emprunteur.nom + " a emprunté le media : " + media.nom)
            return redirect("bibliothequaire")
        else:
            return redirect('emprunt')
    else:
        if media.disponible:
            membres = Membre.objects.all()
            aujourdhui = datetime.date.today()
            formatted_date = aujourdhui.strftime("%Y-%m-%d")
            return render(request,
                          'emprunt.html',
                          {'media': media,
                           'membres': membres,
                           'aujourdhui': formatted_date})
        else:
            return redirect("bibliothequaire")


@login_required
def rentrer(request, id):
    media = Media.objects.get(pk=id)
    emprunteur = media.idEmprunteur
    media.disponible = True
    media.dateEmprunt = None
    media.idEmprunteur = None
    if emprunteur:
        emprunteur.nbEmprunt -= 1
        if emprunteur.nbEmprunt <= 3:
            emprunteur.bloque = False
        emprunteur.save()
    media.save()
    logger.info("Le media " + media.nom + "  a été rentré")
    return redirect("bibliothequaire")
