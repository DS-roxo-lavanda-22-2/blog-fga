# Generated by Django 4.1.4 on 2023-01-17 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]