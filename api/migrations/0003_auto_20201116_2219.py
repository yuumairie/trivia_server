# Generated by Django 3.1.2 on 2020-11-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='trivia',
            name='explanation',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='trivia',
            name='content',
            field=models.TextField(max_length=50),
        ),
    ]
