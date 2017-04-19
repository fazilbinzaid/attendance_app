from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

from accounts.models import Teacher, Student, Batch, AuthUser
from accounts.forms import UserForm

# Create your views here.

class LoginView(View):
	template_name = 'accounts/login.html'

	def get(self, request, *args, **kwargs):
		# print(request.POST)
		return render(request, self.template_name, {})

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
	# template_name = 'accounts/login.html'

	def get_context_data(self, **kwargs):
		return super(UserRegisterView, self).get_context_data(**kwargs)

	def post(self, request, *args, **kwargs):
		form_data = UserForm(request.POST)
		context = self.get_context_data(**kwargs)
		context['form'] = form_data
		if form_data.is_valid():
			username = form_data.cleaned_data['username']
			email = form_data.cleaned_data['email']
			password = form_data.cleaned_data['password']
			print('-'*25, form_data)
			user = AuthUser.objects.create_user(**form_data.cleaned_data)
			return HttpResponse('DOne!')
		return HttpResponse('Not Done')