# Generated by Django 5.0.1 on 2025-03-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GDG', '0004_android_development_questions_firebase_questions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='android_development_result',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='firebase_result',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='flutter_result',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='gemini_result',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='kaggle_result',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='kotlin_result',
            field=models.IntegerField(null=True),
        ),
    ]
