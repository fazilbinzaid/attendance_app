from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Teacher, Student, Batch, AuthUser
from accounts.forms import UserForm, StudentForm, TeacherForm
from attendance.models import Subject, Hour

import json

# Create your views here.

class BatchHourView(TemplateView):
    template_name = 'attendance/batch-hour.html'

    def get_object(self, pk, model):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        teacher = Teacher.objects.get(user__username=request.user.username)
        batch = self.get_object(pk, Batch)
        subjects = teacher.subjects.filter(batch=batch)
        students = batch.students.order_by('roll_no')
        context['hours'] = [item[1] for item in Hour.HOURS]
        context['subjects'] = subjects
        context['teacher'] = teacher
        context['batch'] = batch
        context['students'] = students
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        batch_id = request.POST.get('batch')
        batch = self.get_object(batch_id, Batch)
        hour_id = request.POST.get('hour')
        print(hour_id)
        data = json.loads(request.POST.get('attendance'))
        print(data)
        for student_id in data:
            pass
