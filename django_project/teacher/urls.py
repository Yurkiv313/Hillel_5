from django.urls import path

from . import views

urlpatterns = [
    path("view_teacher/", views.view_teacher, name="view_teacher"),
]
