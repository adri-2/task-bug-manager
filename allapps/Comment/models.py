from django.db import models
from allapps.Reponsebug.models import BugResponse
from django.conf import settings

class CommentResponse(models.Model):
    # reponse_bug = models.ForeignKey(ReponseBug, on_delete=models.CASCADE, related_name="reponse")  # Réponse liée
    response_bug = models.ForeignKey(BugResponse, on_delete=models.CASCADE, related_name="responses")  # Réponse liée

    # auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)  # Auteur
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)  # Auteur

    # auteur_client = models.ForeignKey('Customers.Customer', on_delete=models.SET_NULL, null=True, blank=True)  # Auteur client
    content = models.TextField()  # Contenu

    # date_creation = models.DateTimeField(auto_now_add=True)  # Date de création
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création

    def __str__(self):
        return f"Comment by {self.author} on {self.response_bug}"
