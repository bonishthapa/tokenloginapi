# Generated by Django 3.1.6 on 2021-03-21 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newuser', '0003_newuser_is_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='user_name',
            new_name='username',
        ),
    ]
