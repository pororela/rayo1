# Generated by Django 4.2.1 on 2023-06-29 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0002_contacto_alter_profesional_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=50)),
                ('diagnóstico', models.TextField()),
                ('materiales', models.TextField()),
                ('foto', models.ImageField(null=True, upload_to='Profesional')),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appweb.profesional')),
            ],
        ),
    ]