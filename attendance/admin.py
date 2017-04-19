from django.contrib import admin
from attendance.models import Subject, Hour, BatchTeacherMapping, BatchSubjectMapping

# Register your models here.

admin.site.register(Subject)
admin.site.register(Hour)
admin.site.register(BatchTeacherMapping)
admin.site.register(BatchSubjectMapping)
