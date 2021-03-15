from django.db import models

# Create your models here.

class Students(models.Model):
    initials = models.CharField(max_length=10)
    location = models.CharField(max_length=10)
    letter = models.TextField()

    def __str__(self):
        return self.initials