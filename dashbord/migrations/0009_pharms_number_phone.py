# Generated by Django 4.0.6 on 2022-09-15 15:06

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0008_alter_pharms_de_garde_pharm'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharms',
            name='number_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
