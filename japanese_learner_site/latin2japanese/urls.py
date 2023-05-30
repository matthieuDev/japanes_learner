from django.urls import path

from . import views

urlpatterns = [
    path("", views.latin2japanese_question, name="latin2japanese_question"),
]