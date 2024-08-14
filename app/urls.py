from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("timeline/", views.timeline, name="timeline"),
    path("timeline/add_post/", views.add_post, name="add_post"),
    path("reminder/", views.reminder, name="reminder"),
    path("toggle_like/<int:post_id>/", views.toggle_like, name="toggle_like"),
    path("timeline/comment/<int:post_id>/", views.comment, name="comment"),
    path("chat/", views.chat, name="chat"),
    path("chat/search_users/", views.search_users, name="search_users"),
    path("chat/create_table/", views.create_chat, name="create.chat"),
    path("chat/<int:send_chat_id>/", views.message, name="message"),
    path("tag_list/", views.tag_list, name="tag_list"),
    path("profile/", views.profile, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)