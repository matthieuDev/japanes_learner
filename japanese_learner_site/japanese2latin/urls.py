from django.urls import path

from . import views

urlpatterns = [
    path("", views.japanese2latin_question, name="japanese2latin_question"),
]