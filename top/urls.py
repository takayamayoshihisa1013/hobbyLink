from django.urls import path
from . import views

urlpatterns = [
    path("", views.top, name="hobbyLink_top")
]