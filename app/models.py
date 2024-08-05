from django.db import models
from user.models import User

# Create your models here.

class Post_data(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)
    post_text = models.TextField()
    # def __str__(self):
        # return self.user_id

class Comment(models.Model):
    post_id = models.ForeignKey(Post_data, on_delete=models.CASCADE)
    comment_text = models.TextField()

class Like(models.Model):
    post_id = models.ForeignKey(Post_data, on_delete=models.CASCADE)
    like_num = models.IntegerField(default=0)
    
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