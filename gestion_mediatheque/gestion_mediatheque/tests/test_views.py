import pytest
from django.urls import reverse
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestViews:
    def test_accueil_view(self, client):
        url = reverse('accueil')
        response = client.get(url)
        assert response.status_code == 200

    @pytest.fixture
    def authenticated_user(self, client):
        user = User.objects.create_user(username='testuser', password='12345')
        client.login(username='testuser', password='12345')
        return user

    def test_bibliothequaire_view(self, client, authenticated_user):
        url = reverse('bibliothequaire')
        response = client.get(url)
        assert response.status_code == 200
