# Generated by Django 4.2.3 on 2023-12-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': 'entrada', 'verbose_name_plural': 'entradas'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(null=True, verbose_name='Contenido'),
        ),
    ]
