from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.models import Teacher, Student, Batch, AuthUser
from accounts.forms import UserForm, StudentForm, TeacherForm
from attendance.models import Subject, Hour

# Create your views here.

def username_check(request):
	if request.is_ajax():
		check = request.GET.get('username')
		if check:
			if AuthUser.objects.filter(username=check).exists():
				return HttpResponse(False)
			return HttpResponse(True)


def get_user_object(username):
	try:
		return Teacher.objects.get(user__username=username)
	except Teacher.DoesNotExist:
		try:
			return Student.objects.get(user__username=username)
		except Student.DoesNotExist:
			return HttpResponse("Not Found!.")


class LoginView(TemplateView):
	template_name = 'accounts/login.html'

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		if not request.user.is_authenticated():
			return render(request, self.template_name, context)
		return redirect(reverse('accounts:dashboard'))

	def post(self, request, *args, **kwargs):
		post = request.POST
		username = post['lg_username']
		password = post['lg_password']
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			if request.user.is_authenticated():
				return redirect(reverse('accounts:dashboard'))
		return HttpResponse('Not Done')


class LogoutView(View):

	def get(self, request, *args, **kwargs):
		logout(request)
		url = reverse('accounts:login')
		return redirect(url)


class UserRegisterView(TemplateView):

# To be changed when completed.
# The current function returns a user even if it exists.
# TO DO
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
			# Check whether the user already exists.
			user_object = self.get_or_create_user(form_data.cleaned_data)
			user = authenticate(username=username, password=password)
			login(request, user)
			Student.objects.create(user=request.user)
			return redirect(reverse('accounts:edit-bio-view'))
		return HttpResponse('Not.. Done')


class EditBioView(TemplateView):
	template_name = 'accounts/edit-bio.html'

	def get_object(self, username):
		try:
			instance = Student.objects.get(user__username=username)
			form = StudentForm(instance=instance)
			return {
				'instance': instance,
				'form': form
			}
		except Student.DoesNotExist:
			try:
				instance = Teacher.objects.get(user__username=username)
				form = TeacherForm(instance=instance)
				return {
					'instance': instance,
					'form': form
				}
			except Teacher.DoesNotExist:
				return None

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect(reverse('accounts:login'))
		username = request.user.username
		user = self.get_object(username)
		context = self.get_context_data(**kwargs)
		form = StudentForm(instance=user['instance'])
		context['form'] = user['form']
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		username = request.user.username
		user = self.get_object(username)
		instance = user['instance']
		if type(instance) == Student:
			instance.roll_no = request.POST.get('roll_no', instance.roll_no)
			instance.guardian_name = request.POST.get('guardian_name', instance.guardian_name)
			instance.first_name = request.POST.get('first_name', instance.first_name)
			instance.last_name = request.POST.get('last_name', instance.last_name)
			instance.register_no = request.POST.get('register_no', instance.register_no)
			instance.address = request.POST.get('address', instance.address)
			instance.contact_no = request.POST.get('contact_no', instance.contact_no)
			batch_id = request.POST.get('batch', instance.batch)
			if batch_id:
				instance.batch = Batch.objects.get(id=int(batch_id))
			instance.save()
			return JsonResponse({
				'message': 'Data have been updated successfully.',
				'status': 200
			})
		elif type(instance) == Teacher:
			instance.first_name = request.POST.get('first_name', instance.first_name)
			instance.last_name = request.POST.get('last_name', instance.last_name)
			instance.guardian_name = request.POST.get('guardian_name', instance.guardian_name)
			instance.contact_no = request.POST.get('contact_no', instance.contact_no)
			instance.address = request.POST.get('address', instance.address)
			instance.city = request.POST.get('city', instance.city)
			instance.state = request.POST.get('state', instance.state)
			instance.save()
			return JsonResponse({
				'message': 'Data have been updated successfully.',
				'status': 200
			})
		return JsonResponse({
				'message': 'This shit has gone crazy!.',
				'status': 500
		})

class StaffRegisterView(TemplateView):
	template_name = 'accounts/staff-register.html'

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		user_form = UserForm(request.POST)
		teacher_form = TeacherForm(request.POST)
		if user_form.is_valid():
			username = user_form.cleaned_data['username']
			password = user_form.cleaned_data['password']
			user_object = AuthUser.objects.create_user(**user_form.cleaned_data)
			user = authenticate(username=username, password=password)
			login(request, user)
		if teacher_form.is_valid():
			Teacher.objects.create(user=request.user, **teacher_form.cleaned_data)
			return redirect(reverse('accounts:dashboard'))
		return HttpResponse("Not DONE!")


class DashBoardView(TemplateView):

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		username = request.user.username
		user = get_user_object(username)
		context['user'] = user
		if type(user) == Teacher:
			batches = Batch.objects.filter(id__in=user.subjects.values_list('batch'))
			context['batches'] = batches
			return render(request, 'attendance/teacher/dashboard.html', context)
		elif type(user) == Student:
			subjects = Subject.objects.filter(batch=user.batch)
			context['subjects'] = subjects
			return render(request, 'attendance/student/dashboard.html', context)
