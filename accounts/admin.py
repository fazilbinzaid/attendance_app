from django.contrib import admin
from accounts.models import AuthUser, Teacher, Batch, Student, Course
# Register your models here.

admin.site.register(AuthUser)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(Course)
