from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import ClassInfo, Student
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'index.html'
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
