# Generated by Django 4.2.13 on 2024-08-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_user_groups_remove_user_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_id',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
