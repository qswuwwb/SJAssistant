from django.conf.urls import url
from .views import AttendanceList, attendanceCreate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', AttendanceList.as_view()),
    # url(r'^submit/', login_required(AttendanceCreate.as_view(template_name='Attendance/attendance_form.html')))
    url(r'^submit/', attendanceCreate)
]