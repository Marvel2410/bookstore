from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Salesperson(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio...")

    def __str__(self):
        return f"Profile of {self.username.username}"
