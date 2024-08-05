from django.contrib import admin
from django.urls import path
from gestion_mediatheque import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name="accueil"),
    path('accueil/', views.accueil, name="accueil"),
    path('connexion/', views.connexion, name="connexion"),
    path('bibliothequaire/', views.bibliothequaire, name="bibliothequaire"),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('createmember/', views.createMember, name='createmember'),
    path('supprimer_membre/<int:id>/', views.supprimerMembre, name='supprimer_membre'),
    path('update_member/<int:id>/', views.update_member, name='update_member'),
    path('supprimer_livre/<int:id>/', views.supprimerLivre, name='supprimer_livre'),
    path('update_livre/<int:id>/', views.updateLivre, name='update_livre'),
    path('add_livre/', views.add_livre, name='add_livre'),
    path('supprimer_cd/<int:id>/', views.supprimerCD, name='supprimer_cd'),
    path('update_cd/<int:id>/', views.updateCD, name='update_cd'),
    path('add_cd/', views.add_cd, name='add_cd'),
    path('supprimer_dvd/<int:id>/', views.supprimerDvd, name='supprimer_dvd'),
    path('update_dvd/<int:id>/', views.updateDvd, name='update_dvd'),
    path('add_dvd/', views.add_dvd, name='add_dvd'),
    path('supprimer_jeuxplateaux/<int:id>/', views.supprimerJeuxPlateaux, name='supprimer_jeuxplateaux'),
    path('update_jeuxplateaux/<int:id>/', views.updateJeuxPlateaux, name='update_jeuxplateaux'),
    path('add_jeuxplateaux/', views.add_jeuxplateux, name='add_jeuxplateaux'),
    path('emprunt/<int:id>/', views.emprunt, name='emprunt'),
    path('rentrer/<int:id>/', views.rentrer, name='rentrer')
]
