# Generated by Django 4.2.13 on 2024-06-06 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrar',
            fields=[
                ('id_usuario', models.AutoField(db_column='id_usuario', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
