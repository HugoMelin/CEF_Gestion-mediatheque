from gestion_mediatheque.forms import ConnexionUser, AddLivre


class TestForms:
    def test_connexion_user_form_valid(self):
        form = ConnexionUser(data={
            'name': 'testuser',
            'password': 'testpass'
        })
        assert form.is_valid()

    def test_add_livre_form_valid(self):
        form = AddLivre(data={
            'nom': 'Test Livre',
            'auteur': 'Auteur Test'
        })
        assert form.is_valid()
        