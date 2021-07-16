from django.db import models
from django.urls import reverse
# Create your models here.

class Wishlist(models.Model):
    definition = models.CharField(max_length=100)
    def __str__(self):
        return self.definition
    def get_absolute_url(self):
        return reverse('home')
