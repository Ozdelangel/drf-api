from ssl import create_default_context
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model

class Fighters(models.Model):
    owner_of_contrib = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Create your models here.
