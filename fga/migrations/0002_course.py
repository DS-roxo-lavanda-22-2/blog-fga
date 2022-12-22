# Generated by Django 4.1.3 on 2022-12-22 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('duration', models.IntegerField()),
                ('description', models.CharField(max_length=150)),
                ('credit_number', models.IntegerField()),
                ('icon', models.CharField(max_length=150)),
            ],
        ),
    ]
