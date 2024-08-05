from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("timeline/", views.timeline, name="timeline"),
    path("timeline/add_post/", views.add_post, name="add_post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)