# Generated by Django 4.2.1 on 2023-07-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0010_remove_atencion_estadoatencion_atencion_aceptada_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('Informacion_profecional', models.TextField()),
                ('datosDeContacto', models.TextField()),
                ('foto', models.ImageField(null=True, upload_to='Profesional')),
            ],
        ),
    ]