# Generated by Django 2.2.7 on 2019-11-21 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pelu', '0010_peluquero_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pelu.Cliente')),
                ('peluquero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pelu.Peluquero')),
                ('servicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pelu.Servicio')),
            ],
        ),
    ]
