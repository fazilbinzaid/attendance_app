from django.conf.urls import url, include
from accounts.views import (LoginView, UserRegisterView, LogoutView,
							StudentView,
							)

urlpatterns = [
	
	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^logout/$', LogoutView.as_view(), name='logout'),
	url(r'^register/$', UserRegisterView.as_view(), name='register'),
	url(r'^user-profile/$', StudentView.as_view(), name='student-view'),

]