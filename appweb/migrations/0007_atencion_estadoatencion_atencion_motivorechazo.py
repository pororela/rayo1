# Generated by Django 4.2.1 on 2023-06-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0006_rename_numero_atencion_atencion_numero'),
    ]

    operations = [
        migrations.AddField(
            model_name='atencion',
            name='estadoAtencion',
            field=models.IntegerField(choices=[[0, 'pendiente'], [1, 'Aceptada'], [2, 'Rechazada']], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='atencion',
            name='motivoRechazo',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
