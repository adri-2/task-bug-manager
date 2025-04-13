from django.db import models
from django.urls import reverse
from allapps.Bug.models import BugReport
from django.conf import settings

class BugResponse(models.Model):
    """Model definition for a response to a bug report."""

    # bug = models.ForeignKey(BugReport, on_delete=models.CASCADE, related_name="reponses")  # Bug lié
    bug = models.ForeignKey(BugReport, on_delete=models.CASCADE, related_name="responses")

    # auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Auteur de la réponse
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # contenu = models.TextField()  # Contenu de la réponse
    content = models.TextField()

    # validee = models.BooleanField(default=False)  # Si la solution est acceptée
    is_approved = models.BooleanField(default=False)

    # date_creation = models.DateTimeField(auto_now_add=True)  # Date de création
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response by {self.author} for bug: {self.bug}"

    def get_absolute_url(self):
        return reverse("bug_response_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Bug Response"
        verbose_name_plural = "Bug Responses"
