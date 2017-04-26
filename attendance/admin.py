from django.contrib import admin
from attendance.models import (Subject, Hour,
                               )

# Register your models here.

admin.site.register(Subject)
admin.site.register(Hour)
