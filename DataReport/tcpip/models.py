from django.db import models

# Create your models here.

class tcpdata(models.Model):
    values = models.DecimalField(max_digits=50, decimal_places=5, default="")

    def __str__(self):
        return self.values
