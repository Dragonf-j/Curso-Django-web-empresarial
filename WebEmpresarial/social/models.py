from django.db import models

# Create your models here.
class Link(models.Model):
    Key = models.SlugField(verbose_name='Nombre Clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='Red Social', max_length=200)
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')
    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['created']
    def __str__(self):
        return self.name