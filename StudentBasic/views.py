from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import ClassInfo, Student
from django.urls import reverse
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth import authenticate, login
from django import forms
from suit.widgets import SuitDateWidget
from django.contrib.admin import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, ButtonHolder, Row, Field, HTML
from crispy_forms.bootstrap import InlineField

class IndexView(ListView):
    template_name = 'Attendance/attendance_list.html'
    context_object_name = 'class_list'

    def get_queryset(self):
        return ClassInfo.objects.order_by('id')

def classInfo(request, class_id):
    # try:
    #     student_list = Student.objects.filter(class_info=class_id)
    # except Student.DoesNotExist:
    #     raise Http404("班级不存在")
    student_list = get_list_or_404(Student, class_info=class_id)
    return render(request, 'detail.html', {'student_list': student_list})

# class StudentForm()

class StudentCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.field_template = 'bootstrap3/layout/inline_field.html'

        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-2'
        self.helper.layout = Layout(
            Fieldset('基本信息',
                'name', 'gender', 'id_number',
                'continent', 'city'
            ),
            Fieldset('联系方式',
                'phone_number', 'qq_number', 'contact', 'contact_phone',
            ),
            Fieldset('教育背景',
                'education', 'education_type', 'graduated_school', 'discipline',
                'graduated_date', 'cet_level',
            ),
            Fieldset('报名信息',
                'registration_center', 'class_info'
                     )
        )

        self.helper.add_input(Submit('submit', '确认提交'))
    class Meta:
        model = Student
        exclude = []

        widgets = {
            # 'graduated_date': widgets.AdminDateWidget()
        }


class StudentCreate(CreateView):
    template_name = "student_create.html"
    form_class = StudentCreateForm
    def get_success_url(self):
        return reverse('createSuccess')
    # def get_form(self, form_class=None):
    #     # form = super(StudentCreate, self).get_form(form_class)
    #     # form.fields['graduated_date'].widget.attrs.update({'class': 'datepicker'})
    #     form = StudentCreateForm()
    #     return form

class StudentCreateSuccess(TemplateView):
    template_name = 'student_create_success.html'
