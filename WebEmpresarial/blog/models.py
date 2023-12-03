from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    def __str__(self):
        return self.name


class post(models.Model):
    tittle = models.CharField(max_length=200, verbose_name='Titulo')
    subttile = models.CharField(max_length=200, verbose_name='Titulo')
    published = models.DateTimeField(default=now, verbose_name='Fecha de publicacion')
    image = models.ImageField(upload_to='blog', null=True, blank=True, verbose_name='Imagen')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='autor')
    categories = models.ManyToManyField(category, verbose_name="categorías")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name='entrada'
        verbose_name_plural='entradas'
    def __str__(self):
        return self.name