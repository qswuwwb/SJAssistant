from django.contrib import admin
from django.forms import ModelForm
from suit.widgets import HTML5Input
from .models import Attendance
from StudentBasic.models import Assistant

class AttendanceForm(ModelForm):
    class Meta:
        widgets = {
            'date': HTML5Input(input_type='date')
        }

class AttendanceAdmin(admin.ModelAdmin):
    form = AttendanceForm
    fields = ('date', 'type', 'reason')
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
