from django.conf.urls import url, include
from accounts.views import LoginView, UserRegisterView, LogoutView

urlpatterns = [
	
	url(r'^login/', LoginView.as_view(), name='login'),
	url(r'^register/', UserRegisterView.as_view(), name='register'),
	url(r'^logout/', LogoutView.as_view(), name='logout'),


]