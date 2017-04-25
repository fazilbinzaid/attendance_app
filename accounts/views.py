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

class LoginView(TemplateView):
	template_name = 'accounts/login.html'

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		if request.user.is_authenticated():
			return HttpResponse("DOne")
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
			return AuthUser.objects.create_user(**data)

	def post(self, request, *args, **kwargs):
		form_data = UserForm(request.POST)
		context = self.get_context_data(**kwargs)
		if form_data.is_valid():
			username = form_data.cleaned_data['username']
			email = form_data.cleaned_data['email']
			password = form_data.cleaned_data['password']
			user_object = self.get_or_create_user(form_data.cleaned_data)
			user = authenticate(username=username, password=password)
			login(request, user)
			Student.objects.create(user=request.user)
			return redirect(reverse('accounts:student-view'))
		return HttpResponse('Not.. Done')


class StudentView(TemplateView):
	template_name = 'accounts/student_edit_bio.html'

	def get_object(self, username):
		try:
			return Student.objects.get(user__username=username)
		except Student.DoesNotExist:
			return None

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect(reverse('accounts:login'))
		username = request.user.username
		student = self.get_object(username)
		context = self.get_context_data(**kwargs)
		form = StudentForm(instance=student)
		context['form'] = form
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		username = request.user.username
		instance = self.get_object(username)
		instance.roll_no = request.POST.get('roll_no', instance.roll_no)
		instance.guardian_name = request.POST.get('guardian_name', instance.guardian_name)
		instance.full_name = request.POST.get('full_name', instance.full_name)
		instance.register_no = request.POST.get('register_no', instance.register_no)
		instance.address = request.POST.get('address', instance.address)
		instance.contact_no = request.POST.get('contact_no', instance.contact_no)
		batch_id = request.POST.get('batch', instance.batch)
		instance.batch = Batch.objects.get(id=int(batch_id))
		instance.save()
		return JsonResponse({
			'message': 'Data have been updated successfully.',
			'status': 200
		})

class TeacherView(TemplateView):
	template_name = 'accounts/teacher_register.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})
