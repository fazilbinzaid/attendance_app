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
    template_name = 'attendance/teacher/new-attendance.html'

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
    template_name = "attendance/teacher/batch-detail.html"

    def get_object(self, pk, model):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(BatchDetailView, self).get_context_data(**kwargs)
        teacher = Teacher.objects.get(user__username=self.request.user.username)
        context['teacher'] = teacher
        hour_nos = Hour.HOURS
        context['hour_nos'] = hour_nos
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


def get_history_data(request):
    if request.is_ajax():
        data = request.GET
        # print(data)
        batch_id = data.get("batch_id")
        year = data.get("year")
        month = data.get("month")
        day = data.get("day")
        hour = data.get("hour")
        # print(batch_id, year, month, day)
        batch = Batch.objects.get(id=batch_id)
        subject = batch.subjects.get(teacher=Teacher.objects.get(user__username=request.user.username))
        # print(subject)
        hours = Hour.objects.filter(date__year=year,
                                    date__month=month,
                                    date__day=day,
                                    student__batch=batch,
                                    subject=subject,
                                    code=hour).values(
                                                      'code',
                                                      'is_present',
                                                      'student__pk',
                                                      'student__roll_no',
                                                      'student__first_name',
                                                      'student__last_name',
                                                      ).order_by('student__roll_no')
        return JsonResponse({'results': list(hours)})



class EditAttendanceView(TemplateView):
    template_name = 'attendance/teacher/edit-attendance.html'

    def get_object(self, pk, model):
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            raise Http404

# TO DO
# Using a calendar get every attendance ever registered.
# But can only edit those registered within couple of days.
    def get_context_data(self, **kwargs):
        context = super(EditAttendanceView, self).get_context_data(**kwargs)
        self.teacher = Teacher.objects.get(user__username=self.request.user.username)
        context['teacher'] = self.teacher
        hour_nos = Hour.HOURS
        context['hour_nos'] = hour_nos
        return context

    def get(self, request, pk, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        teacher = context['teacher']
        self.batch = self.get_object(pk, Batch)
        self.subject = Subject.objects.get(teacher=teacher, batch=self.batch)
        context['subject'] = self.subject
        context['batch'] = self.batch
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        teacher = context['teacher']
        print(request.POST)
        data = request.POST
        batch_id, hour_code = data.get('batch'), data.get('hour')
        day_id, month_id, year_id = data.get('day'), data.get('month'), data.get('year')
        att_data = json.loads(request.POST.get('attendance'))
        batch = Batch.objects.get(pk=batch_id)
        subject = teacher.subjects.get(batch=batch)
        for student_id in att_data:
            student = self.get_object(student_id, Student)
            hour_object = Hour.objects.get(date__day=day_id,
                                           date__month=month_id,
                                           date__year=year_id,
                                           subject=subject,
                                           student=student,
                                           code=hour_code)
            hour_object.is_present = bool(int(att_data[student_id]))
            hour_object.save()
        return JsonResponse({
            'message': 'Data have been successfully edited!.',
            'status': 200
        })
