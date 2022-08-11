from django.db import models

# Create your models here.

class Correo(models.Model):
    correo = models.CharField(max_length=300)

    def serialize(self):
        return {
            "id": self.id,
            "correo": self.correo
        }
    def __str__(self):
        return self.correo