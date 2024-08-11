from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.http import JsonResponse
from django.db.models import Prefetch
from .models import Post_data, Image, Like, Comment, Chat, ChatMember, Message
from user.models import User
import os


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Like, Post_data
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

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
    # ユーザーインスタンスを獲得してからじゃないとだめらしい。
    user = User.objects.get(user_id=request.session["user_id"])
    
    if request.method == "POST":
        post_text = request.POST.get("post_text")
        tag = request.POST.get("tag")
        post_files = request.FILES.getlist("post_images")
        print(post_text, tag, post_files)
        
        new_post = Post_data(
            user_id=user,
            post_text=post_text
        )
        new_post.save()
        
        # 新しく追加したpost_idを取得する
        new_post_id = Post_data.objects.get(id=new_post.id)
        print(new_post_id)
        
        # new_post_like = Like(
        #     post_id=new_post_id,
        #     user_id=user  # ここで正しいUserインスタンスを渡す
        # )
        # new_post_like.save()
        
        post_img_dir = os.path.join(settings.BASE_DIR, "app/static/images/post_img")
        if not os.path.exists(post_img_dir):
            os.makedirs(post_img_dir)
        
        for file in post_files:
            file_path = os.path.join(post_img_dir, file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            
            print(file)
            
            new_post_img = Image(
                post_id=new_post_id,
                filename=file.name
            )
            
            new_post_img.save()
    
        return redirect("/hobbyLink/timeline/")
    else:
        user_id = user.profile_id
        print(user_id)
        if user_id is None or user_id:
            user_id = user.user_id
        
    
        
    context = {
        "user_name":request.session["user_name"],
        "user_id":user_id
    }
            
    return render(request, "add_post.html", context)

def comment(request, post_id):
    print(post_id)
    
    if request.method == "POST":
        
        comment_text = request.POST.get("comment")
        print(comment_text)
        
        post_data_id = Post_data.objects.get(id=post_id)
        user = User.objects.get(user_id=request.session["user_id"])
        
        print(post_data_id, "post_data_id")
        
        new_comment = Comment(
            post_id = post_data_id,
            comment_text = comment_text,
            user_id = user
        )
        
        new_comment.save()
        
        return redirect(f"/hobbyLink/timeline/comment/{post_id}/")
    
    post = Post_data.objects.get(id=post_id)
    like = Like.objects.filter(post_id=post_id).count()
    
    post_comment_data = Post_data.objects.filter(id__icontains=post_id).prefetch_related(
        Prefetch("comment_set", queryset=Comment.objects.filter(post_id=post)),
    ).first()
    
    comments = post_comment_data.comment_set.all()
    
    print(post_comment_data, "post_data")
    
    print(post.post_time)
    
    context = {
        "post": post,
        "post_comment_data":post_comment_data,
        "like": like,
        "comments":comments
    }
    
    return render(request, "comment.html", context)

def toggle_like(request, post_id):
    if 'user_id' not in request.session:
        return JsonResponse({'success': False, 'error': 'User not authenticated'}, status=403)
    
    try:
        post = Post_data.objects.get(id=post_id)
        user_id = request.session['user_id']
        user = User.objects.get(user_id=user_id)
        
        # Like オブジェクトを取得または作成
        like, created = Like.objects.get_or_create(post_id=post, user_id=user)
        
        if not created:
            # 既に「いいね」されている場合、「いいね」を削除
            like.delete()
            liked = False
        else:
            # 「いいね」を追加
            like.like_num += 1
            like.save()
            liked = True
        
        return JsonResponse({'success': True, 'like_count': post.like_set.count(), 'liked': liked})
    except Post_data.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Post not found'}, status=404)
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
    

    
def reminder(request):
    
    return render(request, "reminder.html")


def chat(request):
    
    chat_data = Chat.objects.all().prefetch_related(
        Prefetch("message_set", queryset=Message.objects.all())
    )
    
    for chat in chat_data:
        
        print(chat.name)
        chat_body = Message.objects.filter(chat_id = chat.id)
        # print(chat.id)
        for message in chat.message_set.all():
            print(message.text, message.sender, request.session["user_id"])
            if str(message.sender) == request.session["user_id"]:
                print("おなじ")
    
    
    context = {
        "chat_data": chat_data,
        "login_user":request.session["user_id"]
    }
    
    return render(request, "chat.html", context)

def search_users(request):
    query = request.GET.get("q", "")
    if query:
        print(query)
        users = User.objects.filter(user_name__icontains=query)
        users_data = [{"user_name": user.user_name, "user_id": user.user_id} for user in users]
        print(users_data)  # デバッグ用にサーバーコンソールに出力
        return JsonResponse(users_data, safe=False)
    else:
        return JsonResponse([], safe=False)
    
def create_chat(request):
    if request.method == "POST":
        friend_id = request.GET.get("q", "")
        
        # セッションから現在のユーザーを取得
        my_user = User.objects.get(user_id=request.session["user_id"])
        friend_user = User.objects.get(user_id=friend_id)
        
        # 新しいチャットを作成
        new_chat = Chat(name=friend_user.user_name)
        new_chat.save()
        
        # チャットメンバーとして自分と相手を追加
        ChatMember.objects.bulk_create([
            ChatMember(chat=new_chat, user=my_user),
            ChatMember(chat=new_chat, user=friend_user),
        ])
    
    return HttpResponse("hello")


def message(request, send_chat_id):
    # GETリクエストからメッセージを取得
    message_text = request.GET.get("q", "")
    
    # 現在のユーザーとチャットを取得
    user = User.objects.get(user_id=request.session["user_id"])
    chat = Chat.objects.get(id=send_chat_id)
    
    print(user)
    
    # 新しいメッセージを作成
    new_message = Message(
        chat_id=chat,  # chatオブジェクトを渡す
        text=message_text,
        sender=user  # userオブジェクトを渡す
    )
    
    # メッセージを保存
    new_message.save()
    
    context = {
        "text": new_message.text,
        "sender":new_message.sender.user_name,
        "sender_id": str(new_message.sender.user_id),
        "login_id": request.session["user_id"]
    }
    
    return JsonResponse(context)
