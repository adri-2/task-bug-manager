from django.db import models
from django.conf import settings

class Customer(models.Model):
    # nom = models.CharField(max_length=255)  # Nom
    name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    # telephone = models.CharField(max_length=20, blank=True, null=True)  # Téléphone
    phone = models.CharField(max_length=20, blank=True, null=True)

    # nom_compagny = models.CharField(max_length=60, blank=True, null=True)  # Nom de l'entreprise
    company_name = models.CharField(max_length=60, blank=True, null=True)

    # date_inscription = models.DateTimeField(auto_now_add=True)  # Date d’inscription
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
