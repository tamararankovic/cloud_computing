from django.db import models

class Counter(models.Model):
    count = models.PositiveIntegerField(null=False, default=0)
