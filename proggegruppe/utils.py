from django.core.exceptions import ObjectDoesNotExist
from .models import Course, Lesson


def get_all_courses():
    return Course.objects.all()

def get_all_course_titles():
    return Course.objects.values_list("title", flat=True)


def get_lessons_by_course_title(course_title):
    try:
        course = Course.objects.get(title=course_title)
        lessons = Lesson.objects.filter(course=course)
        return lessons
    except ObjectDoesNotExist:
        return None