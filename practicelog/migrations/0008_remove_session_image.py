# Generated by Django 4.1.7 on 2023-03-30 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practicelog', '0007_alter_session_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='image',
        ),
    ]
