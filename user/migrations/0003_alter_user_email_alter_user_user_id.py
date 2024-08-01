# Generated by Django 4.2.13 on 2024-08-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default='<function uu', editable=False, max_length=15, unique=True),
        ),
    ]
