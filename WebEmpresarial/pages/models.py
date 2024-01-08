from django.db import models

# Create your models here.
class Page(models.Model):
    Titulo = models.CharField(verbose_name='Titulo', max_length=200)
    Content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')

    class Meta:
        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['created']

    def __str__(self):
        return self.Titulo