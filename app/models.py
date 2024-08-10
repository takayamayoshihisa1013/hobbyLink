from django.db import models
from user.models import User
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

def get_current_time():
    return timezone.now()

class Post_data(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)
    post_text = models.TextField()
    # def __str__(self):
        # return self.user_id

class Comment(models.Model):
    post_id = models.ForeignKey(Post_data, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=get_current_time)
    
    def __str__(self):
        return self.comment_text

class Like(models.Model):
    post_id = models.ForeignKey(Post_data, on_delete=models.CASCADE)
    like_num = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE ) 
    
    def __str__(self):
        return self.like_num

class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    favorite_post_id = models.ForeignKey(Post_data, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.favorite_post_id

class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.tag

class Image(models.Model):
    post_id = models.ForeignKey(Post_data, on_delete=models.CASCADE, related_name='images')
    filename = models.CharField(max_length=255)
    
    def __str__(self):
        return self.filename

class Chat(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    is_group = models.BooleanField(default=False)

class ChatMember(models.Model):
    chat = models.ForeignKey(Chat, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='chats', on_delete=models.CASCADE)

class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)



# @receiver(post_save, sender=Chat)
# def add_members_to_chat(sender, instance, created, **kwargs):
#     if created and not instance.is_group:
#         ChatMember.objects.create(chat=instance, user=instance.user1)
#         ChatMember.objects.create(chat=instance, user=instance.user2)