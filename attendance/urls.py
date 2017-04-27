from django.conf.urls import url, include

from attendance.views import BatchHourView

urlpatterns = [

    url(r'^user/class/(?P<pk>[0-9]*)/$', BatchHourView.as_view(), name='teacher-batch-hour'),


]
