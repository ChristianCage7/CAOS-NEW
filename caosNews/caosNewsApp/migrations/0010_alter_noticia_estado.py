# Generated by Django 4.2.13 on 2024-06-24 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caosNewsApp', '0009_alter_noticia_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='estado',
            field=models.IntegerField(choices=[(0, 'Inactivo'), (1, 'Activo'), (2, 'Rechazada')], db_column='estado', default=0),
        ),
    ]