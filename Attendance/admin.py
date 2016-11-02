from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import HTML5Input
from .models import Attendance
from StudentBasic.models import Assistant
import datetime
import time
from django.core import serializers
from import_export.admin import ExportActionModelAdmin
from import_export import resources


def lastWeekAttendance(modeladmin, request, queryset):
    today = datetime.datetime.today()
    last_monday = today - datetime.timedelta(days=today.weekday() + 7)
    last_week_attendance = Attendance.objects.filter(date__range=(last_monday, last_monday + datetime.timedelta(days=6)))
    # Attendance.objects.filter(date__month=)
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

class LastWeekAttendanceFilter(admin.SimpleListFilter):
    title = '上周加班情况汇总'
    parameter_name = '11'

    def lookups(self, request, model_admin):
        return (
            ('1', '上周'),
            ('2', '上月'),
        )

    def queryset(self, request, queryset):
        today = datetime.datetime.today()
        if self.value() == '1':
            last_monday = today - datetime.timedelta(days=today.weekday() + 7)
            return queryset.filter(date__range=(last_monday, last_monday + datetime.timedelta(days=6)))
        if self.value() == '2':
            last_month = time.localtime()[1] - 1 or 12
            return queryset.filter(date__month=last_month)

class AttendanceResource(resources.ModelResource):

    class Meta:
        model = Attendance
        fields = ['id', 'assistant__name', 'type', 'date', 'reason']
    # def dehydrate_assistant(self, attendance):
    #     assistant = attendance.assistant
    #     return attendance.assistant.name

class AttendanceAdmin(ExportActionModelAdmin):
    form = AttendanceForm
    resource_class = AttendanceResource
    fields = ('date', 'type', 'reason')
    # actions = [lastWeekAttendance]
    ordering = ('date',)
    list_display = ('assistant', 'date', 'type', 'reason')
    list_filter = ('assistant__name', LastWeekAttendanceFilter)
    # list_select_related = ('assistant', )


    def save_model(self, request, obj, form, change):
        user = request.user
        assistant = Assistant.objects.get(user__username=user)
        if not change:
            obj.assistant = assistant
        obj.save()

    def get_queryset(self, request):
        qs = super(AttendanceAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # print(qs)
            return qs
        else:
            user = request.user
            assistant = Assistant.objects.get(user__username=user)
            return qs.filter(assistant=assistant)



admin.site.register(Attendance, AttendanceAdmin)
