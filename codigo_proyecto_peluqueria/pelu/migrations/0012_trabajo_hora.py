# Generated by Django 2.2.7 on 2019-11-21 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelu', '0011_trabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='hora',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
