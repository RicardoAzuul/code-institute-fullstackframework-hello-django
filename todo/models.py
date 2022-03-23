from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False) # null=False and blank=False means that neither a user, admin or a program can add a todo item without a name
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
