from django.conf.urls import url, include

from attendance.views import (NewAttendanceView,
                              BatchDetailView,
                              )

urlpatterns = [

    url(r'^user/class/(?P<pk>[0-9]*)/new/$', NewAttendanceView.as_view(), name='new-attendance'),
    url(r'^user/class/(?P<pk>[0-9]*)/$', BatchDetailView.as_view(), name='batch-detail'),


]
