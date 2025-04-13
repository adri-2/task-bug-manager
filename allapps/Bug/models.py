from django.db import models
from django.urls import reverse
from allapps.Users.models import UserProfile
from allapps.Customers.models import Customer
from django.conf import settings


class Category(models.Model):
    """Model definition for Category."""

    title = models.CharField(max_length=32)  # Titre
    type = models.CharField(max_length=32)  # Type
    description = models.CharField(max_length=150)  # Description

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'  # Correction orthographique de "Categorys"

    def __str__(self):
        return self.title


class Tags(models.Model):
    """Model definition for Tags."""

    title = models.CharField(max_length=32)  # Titre

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title


class BugReport(models.Model):
    STATUS_CHOICES = [
        ('nouveau', 'New'),  # Nouveau
        ('en_cours', 'In Progress'),  # En cours
        ('resolu', 'Resolved'),  # Résolu
        ('ferme', 'Closed'),  # Fermé
    ]

    PRIORITY_CHOICES = [
        ('faible', 'Low'),  # Faible
        ('moyenne', 'Medium'),  # Moyenne
        ('haute', 'High'),  # Haute
        ('critique', 'Critical'),  # Critique
    ]

    BUG_TYPE_CHOICES = [
        ('interne', 'Internal Bug'),  # Bug interne
        ('client', 'Client Issue'),  # Problème client
    ]
    
    # STATUT_CHOICES = [
    #     ('nouveau', 'Nouveau'),
    #     ('en_cours', 'En cours'),
    #     ('resolu', 'Résolu'),
    #     ('ferme', 'Fermé'),
    # ]

    # PRIORITE_CHOICES = [
    #     ('faible', 'Faible'),
    #     ('moyenne', 'Moyenne'),
    #     ('haute', 'Haute'),
    #     ('critique', 'Critique'),
    # ]

    # TYPE_CHOICES = [
    #     ('interne', 'Bug interne'),
    #     ('client', 'Problème client'),
    # ]


    title = models.CharField(max_length=255)  # Titre
    description = models.TextField()  # Description
    bug_type = models.CharField(max_length=10, choices=BUG_TYPE_CHOICES, default='client')  # Type de bug
    reporter_employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reported_bugs_employee"  # Employé rapporteur
    )
    reporter_client = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reported_bugs_client"  # Client rapporteur
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nouveau')  # Statut
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='moyenne')  # Priorité
    categories = models.ManyToManyField(Category, blank=True)  # Catégories
    tags = models.ManyToManyField(Tags,blank=True)  # Titre
   
    
    
    created_at = models.DateTimeField(auto_now_add=True)  # Date de création
    updated_at = models.DateTimeField(auto_now=True)  # Date de modification

    def __str__(self):
        return f"{self.title} ({self.get_bug_type_display()})"

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class BugAssignment(models.Model):
    bugs = models.ManyToManyField(BugReport, related_name="assignments")  # Bug(s) assigné(s)
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assigned_bugs_by"  # Assigneur
    )
    assigned_to = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="received_bugs"  # Assigné à
    )
    assigned_at = models.DateTimeField(auto_now_add=True)  # Date d’assignation
    updated_at = models.DateTimeField(auto_now=True)  # Date de modification

    def __str__(self):
        return f"{self.assigned_by} → {self.assigned_to} | Bugs: {[bug.title for bug in self.bugs.all()]}"
