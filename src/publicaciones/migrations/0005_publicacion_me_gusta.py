# Generated by Django 4.2.7 on 2023-12-21 23:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicaciones', '0004_publicacion_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='me_gusta',
            field=models.ManyToManyField(blank=True, related_name='posteos', to=settings.AUTH_USER_MODEL),
        ),
    ]
