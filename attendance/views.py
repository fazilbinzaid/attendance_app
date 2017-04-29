from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from accounts.models import Teacher, Student, Batch, AuthUser
from accounts.forms import UserForm, StudentForm, TeacherForm
from attendance.models import Subject, Hour

import json

# Create your views here.

class NewAttendanceView(TemplateView):
    template_name = 'attendance/new-attendance.html'

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
        subject_id = request.POST.get('subject')
        subject = self.get_object(subject_id, Subject)
        hour_id = request.POST.get('hour')
        data = json.loads(request.POST.get('attendance'))
        for student_id in data:
            student = self.get_object(student_id, Student)
            try:
                hour = Hour.objects.create(code=hour_id, subject=subject, student=student)
            except IntegrityError:
                return JsonResponse({
                "message": "Oops!.. It seems that Attendance have already been registered."
                })
            if int(data[student_id]):
                hour.is_present = True
                hour.save()
        return JsonResponse({
            "message": "Attendance have been registered successfully!."
        })


class BatchDetailView(TemplateView):
    template_name = "attendance/batch-detail.html"

    def get_object(self, pk, model):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(BatchDetailView, self).get_context_data(**kwargs)
        teacher = Teacher.objects.get(user__username=self.request.user.username)
        context['teacher'] = teacher
        return context

    def get(self, request, pk, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        teacher = context['teacher']
        batch = self.get_object(pk, Batch)
        context['batch'] = batch
        subject = teacher.subjects.get(batch=batch)
        context['subject'] = subject
        dates = subject.hours.filter(student__batch=batch).values_list('date').distinct()
        context['dates'] = dates
        return render(request, self.template_name, context)


class EditAttendanceView(TemplateView):
    template_name = 'attendance/edit-attendance.html'

# TO DO
# Using a calendar get every attendance ever registered.
# But can only edit those registered within couple of days.
    def get_context_data(self, **kwargs):
        context = super(EditAttendanceView, self).get_context_data(**kwargs)
        teacher = Teacher.objects.get(user__username=self.request.user.username)
        context['teacher'] = teacher
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        pass
