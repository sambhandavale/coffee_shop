# Generated by Django 4.2.6 on 2024-02-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='no_of_logins',
            field=models.IntegerField(default=0),
        ),
    ]
