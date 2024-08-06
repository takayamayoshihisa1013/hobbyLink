import uuid
from django.db import models

class User(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True)  # ランダムなUUIDを生成
    user_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255 , unique=True)
    password = models.CharField(max_length=100, default="defaultpassword")
    profile_id = models.CharField(max_length=20, null=True, unique=True)

    def __str__(self):
        return str(self.user_id)
