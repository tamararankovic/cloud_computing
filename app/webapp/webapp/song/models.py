from django.db import models

class Song(models.Model):
    title = models.CharField(null=True, max_length=512)
    performedBy = models.CharField(null=True, max_length=50)
    releaseDate = models.DateField(null=True)
    rating = models.DecimalField(null=False, max_digits=3, decimal_places=2)
