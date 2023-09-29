from django.urls import path

from . import views

urlpatterns = [
    path("generate-student/", views.one_user, name="one_user"),
    path("generate-students/", views.students_generate, name="students_generate"),
]
