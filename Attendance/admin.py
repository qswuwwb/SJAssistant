from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import HTML5Input
from .models import Attendance
from StudentBasic.models import Assistant
import datetime
from django.core import serializers

def lastWeekAttendance(modeladmin, request, queryset):
    today = datetime.datetime.today()
    last_monday = today - datetime.timedelta(days=today.weekday() + 7)
    last_week_attendance = Attendance.objects.filter(date__range=(last_monday, last_monday + datetime.timedelta(days=6)))
    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    with open("lastWeekAttendance.json", "w") as out:
        json_serializer.serialize(last_week_attendance, stream = out)

lastWeekAttendance.short_description = "上周加班情况汇总"

class AttendanceForm(ModelForm):
    class Meta:
        widgets = {
            'date': HTML5Input(input_type='date')
        }

class AttendanceAdmin(admin.ModelAdmin):
    form = AttendanceForm
    fields = ('date', 'type', 'reason')
    # actions = [lastWeekAttendance]
    ordering = ('date',)
    list_display = ('assistant', 'date', 'type', 'reason')
    # list_filter = ('assistant__name',)
    list_select_related = ('assistant', )

    def save_model(self, request, obj, form, change):
        user = request.user
        assistant = Assistant.objects.get(user__username=user)
        if not change:
            obj.assistant = assistant
        obj.save()

    def get_queryset(self, request):
        qs = super(AttendanceAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            user = request.user
            assistant = Assistant.objects.get(user__username=user)
            return qs.filter(assistant=assistant)

admin.site.register(Attendance, AttendanceAdmin)
