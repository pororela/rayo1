# Generated by Django 4.2.1 on 2023-06-29 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='profesional',
            name='foto',
            field=models.ImageField(null=True, upload_to='Profesional'),
        ),
    ]
