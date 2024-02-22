# Generated by Django 5.0.1 on 2024-02-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding_lite', '0003_alter_rsvp_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='full_name',
            field=models.CharField(help_text='Enter your Full Name', max_length=100, unique=True),
        ),
    ]
