from .import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("topics/", views.topics, name="topics"),
    path("topic/<int:topic_id>/", views.topic, name='topic'),
    path("new_topic/", views.new_topic, name="new_topic"),
    path("topic/<int:topic_id>/new_entry/", views.new_entry, name="new_entry"),
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
    # path("topic/<int:topic_id>/edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
         

]

