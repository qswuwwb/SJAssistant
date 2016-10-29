from django.contrib import admin

# Register your models here.
from .models import ClassInfo, Student, Assistant, HeadTeacher, City, Continent
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class ClassInfoAdmin(admin.ModelAdmin):
    fields = []

class AssistantInline(admin.StackedInline):
    model = Assistant
    can_delete = False
    verbose_name = "项目经理"

class UserAdmin(BaseUserAdmin):
    inlines = (AssistantInline, )

class StudentAdmin(admin.ModelAdmin):
    # fields = []
    list_display = ('name', 'birthday')

admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Assistant)
admin.site.register(HeadTeacher)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Continent)
admin.site.register(City)
