# Generated by Django 4.1.7 on 2023-02-25 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='password2',
        ),
    ]
