from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Task)
admin.site.register(Submission)
admin.site.register(Badge)
admin.site.register(UserBadge)
admin.site.register(TaskField)