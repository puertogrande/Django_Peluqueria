# Generated by Django 2.2.7 on 2019-11-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelu', '0009_peluquero_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='peluquero',
            name='descripcion',
            field=models.CharField(max_length=500, null=True),
        ),
    ]