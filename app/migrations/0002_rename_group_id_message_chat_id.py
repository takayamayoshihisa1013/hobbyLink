# Generated by Django 4.2.13 on 2024-08-10 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='group_id',
            new_name='chat_id',
        ),
    ]
