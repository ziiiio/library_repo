# Generated by Django 2.2.2 on 2019-06-20 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
