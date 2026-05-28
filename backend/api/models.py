from django.db import models

class EmissionRecord(models.Model):
    source = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.source