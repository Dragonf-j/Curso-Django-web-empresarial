from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    def __str__(self):
        return self.name


class Post(models.Model):
    tittle = models.CharField(max_length=200, verbose_name='Titulo')
    subttile = models.CharField(max_length=200, verbose_name='Subtitulo')
    published = models.DateTimeField(default=now, verbose_name='Fecha de publicacion')
    image = models.ImageField(upload_to='blog', null=True, blank=True, verbose_name='Imagen')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='autor')
    categories = models.ManyToManyField(Category, verbose_name="categorías", related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    content = models.TextField(verbose_name="Contenido", null=True)
    
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']
    def __str__(self):
        return self.tittle