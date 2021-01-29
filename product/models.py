from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title


