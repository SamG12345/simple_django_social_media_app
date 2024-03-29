# Generated by Django 5.0.1 on 2024-01-26 07:57

import django.db.models.deletion
import sham.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sham', '0004_profile_companian_profile_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='self'),
        ),
        migrations.CreateModel(
            name='Lekh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name=sham.models.Profile)),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_by', to='sham.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sham.profile')),
            ],
        ),
    ]
