# Generated by Django 4.0.6 on 2022-08-02 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_commune', models.CharField(choices=[('1', 'Be'), ('2', 'Agoe'), ('3', 'Baguida')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Phams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=250)),
                ('localisation', models.URLField(max_length=150)),
                ('commune', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='dashbord.commune')),
            ],
        ),
    ]
