from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Teacher, Student, Batch, AuthUser
from accounts.forms import UserForm, StudentForm, TeacherForm

# Create your views here.

class BatchHourView(TemplateView):
    template_name = 'attendance/batch-hour.html'

    def get(self, request, pk, *args, **kwargs):
        return render(request, self.template_name, {})
