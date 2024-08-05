import pytest
from gestion_mediatheque.models import Livre, Membre


@pytest.mark.django_db
class TestModels:
    def test_create_livre(self):
        livre = Livre.create("Test Livre", "Auteur Test")
        assert livre.nom == "Test Livre"
        assert livre.auteur == "Auteur Test"

    def test_membre_bloque(self):
        membre = Membre.create("Test Membre")
        membre.nbEmprunt = 3
        membre.save()
        assert membre.bloque == True
