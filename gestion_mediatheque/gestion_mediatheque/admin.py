from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gestion_mediatheque.models import Bibliothequaire

admin.site.register(Bibliothequaire, UserAdmin)
