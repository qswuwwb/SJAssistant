from django.contrib import admin

# Register your models here.
from .models import ClassInfo, Student, Assistant, HeadTeacher

class ClassInfoAdmin(admin.ModelAdmin):
    fields = []


admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(Student)
admin.site.register(Assistant)
admin.site.register(HeadTeacher)