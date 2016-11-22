from django.contrib import admin
from .models import StudentDiscipline
from StudentBasic.models import Student, Assistant, HeadTeacher
from django.db.models import Q

class DisciplineAdmin(admin.ModelAdmin):

    list_display = ('student', 'type', 'operator', 'add_date')
    list_filter = ('student', 'type', 'operator', 'add_date')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.operator = request.user

        obj.save()

    # def get_queryset(self, request):
    #     qs = super(DisciplineAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     else:
    #         return qs.filter(operator__username = request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if not request.user.is_superuser:
            if db_field.name == 'student':
                assistant = Assistant.objects.filter(user__username=request.user)
                head_teacher = HeadTeacher.objects.filter(user__username=request.user)
                kwargs["queryset"] = Student.objects.filter(
                    Q(class_info__assistant = assistant) | Q(class_info__head_teacher = head_teacher)).filter(
                    Q(class_info__is_graduate=False)
                )
        else:
            kwargs["queryset"] = Student.objects.all()
        return super(DisciplineAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(StudentDiscipline, DisciplineAdmin)
