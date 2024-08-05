from django.shortcuts import render
from django.conf import settings
from django.db.models import Prefetch
from .models import Post_data, Image, Like, Comment
from user.models import User
import os
# Create your views here.

# なんの拡張子かみる
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', "avif"}

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def home(request):
    # post_img = 
    posts_with_images = Post_data.objects.prefetch_related("images")
    for post in posts_with_images:
        print(f"Post by {post.user_id.user_name} at {post.post_time}")
        print(f"Text: {post.post_text}")
        print("Images:")
        for image in post.images.all():
            print(image.filename)
    # print(post)
    return render(request, "home.html")

def timeline(request):
    
    post_search = request.GET.get('post_search', '')
    
    # すべてのPost_dataとそれに関連するComment, Like, Imageを取得
    posts_with_related_data = Post_data.objects.filter(post_text__icontains=post_search).prefetch_related(
        'images',
        Prefetch('comment_set', queryset=Comment.objects.all()),
        Prefetch('like_set', queryset=Like.objects.all())
    )
    
    for post in posts_with_related_data:
        print(f"Post by {post.user_id.user_name} at {post.post_time}")
        print(f"Text: {post.post_text}")
        
        # 画像を表示
        print("Images:")
        for image in post.images.all():
            print(image.filename)
        
        # コメントを表示
        print("Comments:")
        for comment in post.comment_set.all():
            print(comment.comment_text)
        
        # いいねを表示
        print("Likes:")
        for like in post.like_set.all():
            print(like.like_num)
    # print(posts_with_related_data)
    context = {
        "posts_with_related_data":posts_with_related_data
    }
    return render(request, "timeline.html", context)

def add_post(request):
    if request.method == "POST":
        post_text = request.POST.get("post_text")
        tag = request.POST.get("tag")
        post_files = request.FILES.getlist("post_images")
        print(post_text,tag,post_files)
        
        # print(request.session["user_id"])
        
        # ユーザーインスタンスを獲得してからじゃないとだめらしい。
        user = User.objects.get(user_id = request.session["user_id"])
        
        new_post = Post_data(
            user_id = user,
            post_text = post_text
        )
        new_post.save()
        
        # 新しく追加したpost_idを取得する
        # これもインスタンスがないとダメと言われた
        new_post_id = Post_data.objects.get(id = new_post.id)
        print(new_post_id)
        
        
        
        new_post_like = Like(
            post_id = new_post_id
        )
        new_post_like.save()
        
        post_img_dir = os.path.join(settings.BASE_DIR, "app/static/images/post_img")
        if not os.path.exists(post_img_dir):
            os.makedirs(post_img_dir)
        
        for file in post_files:
            file_path = os.path.join(post_img_dir, file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                    # print(file.name,"保存")
            
            print(file)
            
            new_post_img = Image(
                post_id = new_post_id,
                filename = file.name
            )
            
            new_post_img.save()
            
        
        
    return render(request, "add_post.html")