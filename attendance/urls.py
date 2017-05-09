from django.conf.urls import url, include

from attendance.views import (NewAttendanceView,
                              BatchDetailView,
                              EditAttendanceView,
                              RecentAttendanceView,
                              get_history_data,
                              )

urlpatterns = [

    url(r'^user/class/(?P<pk>[0-9]*)/new/$', NewAttendanceView.as_view(), name='new-attendance'),
    url(r'^user/class/(?P<pk>[0-9]*)/$', BatchDetailView.as_view(), name='batch-detail'),
    url(r'^user/class/(?P<pk>[0-9]*)/history/$', EditAttendanceView.as_view(), name='batch-history'),
    url(r'^user/class/(?P<pk>[0-9]*)/recent/$', RecentAttendanceView.as_view(), name='batch-recent'),
    url(r'^user/class/get-history/$', get_history_data, name='batch-get-history'),


]
