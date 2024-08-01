# Generated by Django 4.2.13 on 2024-08-01 07:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
