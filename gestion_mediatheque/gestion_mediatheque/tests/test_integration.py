import pytest
from django.urls import reverse
from gestion_mediatheque.models import Livre, Membre


@pytest.mark.django_db
class TestIntegration:
    @pytest.fixture
    def setup_data(self):
        Livre.create("Test Livre", "Auteur Test")
        Membre.create("Test Membre")

    def test_emprunt_process(self, client, authenticated_user, setup_data):
        livre = Livre.objects.first()
        membre = Membre.objects.first()

        # Test emprunt
        url = reverse('emprunt', args=[livre.id])
        response = client.post(url, {'emprunteur': membre.id, 'date': '2024-08-05'})
        assert response.status_code == 302  # Redirect after successful operation

        livre.refresh_from_db()
        membre.refresh_from_db()
        assert livre.disponible == False
        assert membre.nbEmprunt == 1

        # Test retour
        url = reverse('rentrer', args=[livre.id])
        response = client.get(url)
        assert response.status_code == 302

        livre.refresh_from_db()
        membre.refresh_from_db()
        assert livre.disponible == True
        assert membre.nbEmprunt == 0
