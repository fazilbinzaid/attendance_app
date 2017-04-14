from django.contrib import admin
from accounts.models import AuthUser, Teacher
# Register your models here.

admin.site.register(AuthUser)
admin.site.register(Teacher)
