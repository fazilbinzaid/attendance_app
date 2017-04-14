from django.shortcuts import render
from accounts.models import Teacher, Student, Batch
from django.views import View

# Create your views here.

class LoginView(View):
	# template_name = 

	# def get(self, request, *args, **kwargs):
	# 	pass

	def post(self, request, *args, **kwargs):
		print(request.POST)
		
			# return 