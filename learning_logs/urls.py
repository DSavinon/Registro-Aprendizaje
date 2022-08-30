"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

# para que django pueda distinguir entre urls.py files
app_name = "learning_logs"
urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    # Topics Page
    path("topics/", views.topics, name="topics"),
    # Page for a single topic
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    # New Topic
    path("new_topic/", views.new_topic, name="new_topic"),
    # New Entry
    path("new_entry<int:topic_id>/", views.new_entry, name="new_entry"),
    # Editar entries
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]
