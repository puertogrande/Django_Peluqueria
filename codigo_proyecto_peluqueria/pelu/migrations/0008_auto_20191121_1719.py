# Generated by Django 2.2.7 on 2019-11-21 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelu', '0007_auto_20191120_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], default='Mujer', max_length=7),
        ),
    ]