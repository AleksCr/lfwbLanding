from django.db import models


class Token(models.Model):
    token = models.TextField()

    def __str__(self):
        return self.token

# Create your models here.
