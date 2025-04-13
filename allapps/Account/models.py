from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


    
class Account(models.Model):
    """Model definition for Account."""
    username = models.CharField(max_length=36,unique=True)
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    piture_profil = models.ImageField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Account."""

        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        """Unicode representation of Account."""
        pass

    def save(self):
        """Save method for Account."""
        pass

    def get_absolute_url(self):
        """Return absolute url for Account."""
        return ('')

    # TODO: Define custom methods here
    