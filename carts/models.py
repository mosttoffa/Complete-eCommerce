from django.db import models
from django.conf import settings

from product.models import Product

# Create your models here.

User = settings.AUTH_USER_MODEL



class Cart(models.Model):
    user     = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  # SET_NULL: (/ or models.CASCADE) Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL. # CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
    products = models.ManyToManyField(Product, blank=True)
    total    = models.PositiveIntegerField(default=0) 
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


