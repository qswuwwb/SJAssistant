from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView
from .models import Attendance
from StudentBasic.models import Assistant
from django.forms.models import formset_factory
from django.contrib.auth.models import User
from extra_views import ModelFormSetView, FormSetView
from django.forms import ModelForm, TextInput, DateInput, SelectDateWidget, Select
from django.forms.widgets import Input
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Row, Fieldset, Field, Button
from crispy_forms import bootstrap

class MyDateInput(Input):
    input_type = 'date'

class MySelect(Select):
    pass

class AttendanceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Attendance
        fields = ('date', 'type', 'reason')

        widgets = {
            'date': MyDateInput(),
            'type': Select(attrs={'class': 'form-control'}),
            'reason': TextInput(attrs={'class': 'form-control'}),
        }

class AttendanceList(ListView):
    def get_queryset(self):
        user = self.request.user
        assistant = Assistant.objects.filter(user__username=user)
        return Attendance.objects.filter(assistant = assistant)

class AttendanceFormsetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(AttendanceFormsetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_class = 'form-inline'
        self.template = 'bootstrap/table_inline_formset.html'
        # self.field_template = 'bootstrap3/layout/inline_field.html'
        self.layout = Layout(
            'date', 'type', 'reason'
        )
        self.render_required_fields = True
        self.add_input(Submit("submit", "提交"))
        self.add_input(Button("cancel", "取消"))

def attendanceCreate(request):
    template_name = 'Attendance/attendance_form.html'
    AttendanceFormSet = formset_factory(AttendanceForm, extra=2)
    formset = AttendanceFormSet()
    helper = AttendanceFormsetHelper()
    return render(request, template_name, {'formset': formset, 'helper': helper})

