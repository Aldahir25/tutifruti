# Generated by Django 3.2.25 on 2024-10-26 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pp2', '0004_auto_20241026_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='direccionenvio',
            old_name='provincia',
            new_name='distrito',
        ),
    ]
