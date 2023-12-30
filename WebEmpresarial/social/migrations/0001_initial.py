# Generated by Django 4.2.3 on 2023-12-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Key', models.SlugField(max_length=100, unique=True, verbose_name='Nombre Clave')),
                ('name', models.CharField(max_length=200, verbose_name='Red Social')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
            ],
            options={
                'verbose_name': 'enlace',
                'verbose_name_plural': 'enlace',
                'ordering': ['created'],
            },
        ),
    ]
