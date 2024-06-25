# Generated by Django 4.2.13 on 2024-06-24 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('caosNewsApp', '0007_remove_noticia_id_usuario_noticia_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noticias', to=settings.AUTH_USER_MODEL),
        ),
    ]