from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    # email = models.EmailField(unique=True)
    # first_name = models.CharField(max_length=150)
    # last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employé'),
    ], default='employee')
    
    # Surcharge du champ username
    # username = models.CharField(max_length=255, unique=True, blank=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    # def save(self, *args, **kwargs):
    #     if not self.username:  
    #         self.username = f"{self.first_name.lower()}-{self.last_name.lower()}"
    #     super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})    

    def __str__(self):
        return self.username


    
    
