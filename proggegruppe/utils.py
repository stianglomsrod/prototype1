from django.core.exceptions import ObjectDoesNotExist
from .models import Course, Lesson, Task, TaskField


def get_all_courses():
    return Course.objects.all()

def get_all_course_titles():
    return Course.objects.values_list("title", flat=True)

def get_course_by_title(course_title):
    try:
        course = Course.objects.get(title=course_title)
        return course
    except ObjectDoesNotExist:
        return None


def get_course_by_id(course_id):
    try:
        course = Course.objects.get(id=course_id)
        return course
    except ObjectDoesNotExist:
        return None


def get_lessons_by_course_title(course_title):
    try:
        course = Course.objects.get(title=course_title)
        lessons = Lesson.objects.filter(course=course)
        return lessons
    except ObjectDoesNotExist:
        return None
    
def get_lessons_by_course_id(course_id):
    try:
        course = Course.objects.get(id=course_id)
        lessons = Lesson.objects.filter(course=course)
        return lessons
    except ObjectDoesNotExist:
        return None
    

def get_tasks_by_lesson_title(lesson_title):
    try:
        lesson = Lesson.objects.get(title=lesson_title)
        tasks = Task.objects.filter(lesson=lesson)
        return tasks
    except ObjectDoesNotExist:
        return None

def get_tasks_by_lesson_id(lesson_id):
    try:
        lesson = Lesson.objects.get(id=lesson_id)
        tasks = Task.objects.filter(lesson=lesson)
        return tasks
    except ObjectDoesNotExist:
        return None
    
def get_task_by_id(task_id):
    try:
        task = Task.objects.get(id=task_id)
        return task
    except ObjectDoesNotExist:
        return None
    
def get_fields_by_task_id(task_id):
    try:
        task = Task.objects.get(id=task_id)
        fields = TaskField.objects.filter(task=task)
        return fields
    except ObjectDoesNotExist:
        return None
    
def get_lesson_by_id(lesson_id):
    try:
        lesson = Lesson.objects.get(id=lesson_id)
        return lesson
    except ObjectDoesNotExist:
        return None