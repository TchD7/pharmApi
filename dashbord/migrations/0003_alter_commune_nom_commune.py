# Generated by Django 4.0.6 on 2022-08-12 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0002_rename_phams_pharms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commune',
            name='nom_commune',
            field=models.CharField(choices=[('Be', 'Be'), ('Ago', 'Agoe')], max_length=200),
        ),
    ]
