from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# Custom User model
class User(AbstractUser):
    is_pupil = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    # profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    experience_points = models.PositiveIntegerField(default=0)

# Course model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# Lesson model
class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title

# Task model
class Task(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='tasks', on_delete=models.CASCADE)
    description = models.TextField()
    code_snippet = models.TextField()
    
    field_attributes = models.TextField(null=True, blank=True)
    hidden_attributes = models.TextField(null=True, blank=True)
    
    hints = models.TextField(null=True, blank=True)
    solution = models.TextField()
    points = models.PositiveIntegerField()

    def __str__(self):
        return f"Task for {self.lesson.title}"

# Submission model
class Submission(models.Model):
    task = models.ForeignKey(Task, related_name='submissions', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='submissions', on_delete=models.CASCADE)
    submitted_code = models.TextField()
    is_correct = models.BooleanField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.user.username}"

# Badge model
class Badge(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # image = models.ImageField(upload_to='badge_images/')
    criteria = models.TextField()
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.title

# UserBadge model to link badges to users
class UserBadge(models.Model):
    user = models.ForeignKey(User, related_name='user_badges', on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, related_name='user_badges', on_delete=models.CASCADE)
    awarded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.badge.title} awarded to {self.user.username}"