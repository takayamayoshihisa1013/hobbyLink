# Generated by Django 4.2.13 on 2024-08-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.UUIDField(default='<function uu', editable=False, unique=True),
        ),
    ]
