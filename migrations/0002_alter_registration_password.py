# Generated by Django 5.0.1 on 2025-03-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GDG', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
