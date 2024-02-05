from .import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("topics/", views.topics, name="topics"),
    path("topic/<int:topic_id>/", views.topic, name='topic'),
    path("new_topic/", views.new_topic, name="new_topic"),
]
