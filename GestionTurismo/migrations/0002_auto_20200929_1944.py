# Generated by Django 2.2.5 on 2020-09-29 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionTurismo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rut', models.CharField(max_length=14, unique=True)),
                ('Nombre', models.CharField(max_length=30, null=True)),
                ('Apellidos', models.CharField(max_length=30, null=True)),
                ('Edad', models.IntegerField(null=True)),
                ('Nacionalidad', models.CharField(max_length=30, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('Telefono', models.CharField(max_length=12, null=True)),
                ('Nombre_Usuario', models.CharField(default='', max_length=12)),
                ('Contraseña_Usuario', models.CharField(default='', max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
    ]