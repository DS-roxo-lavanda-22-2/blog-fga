# Generated by Django 4.1.4 on 2023-01-22 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fga', '0003_rename_login_login_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
