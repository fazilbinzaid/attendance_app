from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Teacher, Student, Batch, AuthUser
from accounts.forms import UserForm, StudentForm

# Create your views here.

class LoginView(TemplateView):
	template_name = 'accounts/login.html'

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		post = request.POST
		username = post['lg_username']
		password = post['lg_password']
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return HttpResponse('Done')
		return HttpResponse('Not Done')


class LogoutView(View):

	def get(self, request, *args, **kwargs):
		logout(request)
		url = reverse('accounts:login')
		return redirect(url)



class BatchListView(View):
	template_name = 'accounts/dashboard.html'

	def get_context_data(self, **kwargs):
		return super(BatchListView, self).get_context_data(**kwargs)

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		context['batches'] = Batch.objects.all()
		return render(request, self.template_name, context)


class UserRegisterView(TemplateView):

	def get_or_create_user(self, data):
		try:
			return AuthUser.objects.get(username=data['username'])
		except AuthUser.DoesNotExist:
			return AuthUser.objects.create_user(data)

	def post(self, request, *args, **kwargs):
		form_data = UserForm(request.POST)
		context = self.get_context_data(**kwargs)
		if form_data.is_valid():
			# print(form_data)
			username = form_data.cleaned_data['username']
			email = form_data.cleaned_data['email']
			password = form_data.cleaned_data['password']
			# print(form_data.cleaned_data)
			user_object = self.get_or_create_user(form_data.cleaned_data)
			# print(user_object)
			user = authenticate(username=username, password=password)
			# print('-'*29, user)
			# if user:
			login(request, user)
			Student.objects.create(user=request.user)
			url = reverse('accounts:student-view')
			return redirect(url)
		return HttpResponse('Not.. Done')


class StudentView(TemplateView):
	template_name = 'accounts/register.html'

	def get_object(self, username):
		try:
			return Student.objects.get(user__username=username)
		except Student.DoesNotExist:
			return None

	def get(self, request, *args, **kwargs):
		username = request.user.username
		student = self.get_object(username)
		context = self.get_context_data(**kwargs)
		# print(student)
		# batches = Batch.objects.all()
		form = StudentForm(instance=student)
		# print(form)
		context['form'] = form
		# context['batches'] = batches
		context['student'] = student
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		username = request.user.username
		student = self.get_object(username)
		roll_no = request.POST.get('roll_no', student.roll_no)
		guardian_name = request.POST.get('guardian_name', student.guardian_name)
		print(student.roll_no)
		print(roll_no)



