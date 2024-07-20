from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .utils import get_all_courses, get_all_course_titles, get_lessons_by_course_title

# Create your views here.

def index(request):
    return render(request, "proggegruppe/index.html")

def courses(request):
    return render(request, "proggegruppe/courses.html")

def course(request, course):
    lessons = get_lessons_by_course_title(course.capitalize())
    courses = get_all_courses()
    courses_title = get_all_course_titles()
    # courses_stripped = [c.strip() for c in courses]
    if course.capitalize() in courses_title:
        return render(request, "proggegruppe/course.html", {
            "course": course,
            "titles": courses_title,
            "courses": courses,
            "lessons": lessons
            })
    else:
         return render(request, "proggegruppe/404.html")