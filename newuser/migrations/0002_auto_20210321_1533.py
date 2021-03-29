# Generated by Django 3.1.6 on 2021-03-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('newuser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='username',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='newuser',
            name='about',
            field=models.TextField(blank=True, max_length=500, verbose_name='about'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
