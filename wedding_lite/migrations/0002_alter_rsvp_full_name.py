# Generated by Django 5.0.1 on 2024-02-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_lite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='full_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
