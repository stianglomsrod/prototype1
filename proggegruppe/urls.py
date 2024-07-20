from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("courses/", views.courses, name="courses"),
    path("courses/<str:course>/", views.course, name="course"),
    path("courses/<str:course>/lessons", views.lessons, name="lessons"),
    path("courses/<str:course>/<str:lesson>", views.lesson, name="lesson"),
]
