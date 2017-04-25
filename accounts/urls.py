from django.conf.urls import url, include
from accounts.views import (LoginView, UserRegisterView, LogoutView,
							EditBioView, TeacherView,
							)

urlpatterns = [

	url(r'^login/$', LoginView.as_view(), name='login'),
	url(r'^logout/$', LogoutView.as_view(), name='logout'),
	url(r'^register/$', UserRegisterView.as_view(), name='student-register'),
	url(r'^staff-register/$', TeacherView.as_view(), name='staff-register'),
	url(r'^user-profile/$', EditBioView.as_view(), name='edit-bio-view'),

]
