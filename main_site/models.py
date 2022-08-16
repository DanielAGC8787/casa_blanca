from django.db import models
import os

# Create your models here.
def get_image_path(instance, filename):
    return os.path.join('images', filename)


class Correo(models.Model):
    correo = models.CharField(max_length=300)

    def serialize(self):
        return {
            "id": self.id,
            "correo": self.correo
        }
    def __str__(self):
        return self.correo

class Sala(models.Model):
    pic = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    def __str__(self):
        return self.pic.name

class Gabinete(models.Model):
    pic = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    def __str__(self):
        return self.pic.name

class Comedor(models.Model):
    pic = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    def __str__(self):
        return self.pic.name

class Silla(models.Model):
    pic = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    def __str__(self):
        return self.pic.name

class Escritorio(models.Model):
    pic = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    def __str__(self):
        return self.pic.name

class Nino(models.Model):
    pic = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    def __str__(self):
        return self.pic.name