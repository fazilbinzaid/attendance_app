from django.shortcuts import render
from accounts.models import Teacher, Student, Batch
from django.views import View
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.

class LoginView(View):
	template_name = 'login.html'

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

