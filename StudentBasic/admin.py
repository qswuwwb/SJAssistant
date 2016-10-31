from django.contrib import admin

# Register your models here.
from .models import ClassInfo, Student, Assistant, HeadTeacher, City, Continent
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
import time
from StudentBasic.models import GENDER, EDUCATION, EDUCATION_TYPE, CET_LEVEL, CENTER

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

class StudentResource(resources.ModelResource):
    age = fields.Field()
    native_place = fields.Field()
    qq_mail = fields.Field()
    class Meta:
        model = Student
        fields = ('id', 'name', 'gender', 'age', 'native_place',
                  'qq_number', 'qq_mail', 'contact', 'contact_phone',
                  'education', 'education_type', 'graduated_school', 'discipline', 'graduated_date',
                  'cet_level', 'registration_center', 'class_info__name')
        export_order = ('id', 'name', 'gender', 'age', 'native_place',
                  'qq_number', 'qq_mail', 'contact', 'contact_phone',
                  'education', 'education_type', 'graduated_school', 'discipline', 'graduated_date',
                  'cet_level', 'registration_center', 'class_info__name')

    def dehydrate_age(self, student):
        current_year = time.strftime('%Y', time.localtime())
        birth_year = student.birthday()[0:4]
        print(current_year, birth_year)
        return  int(current_year) - int(birth_year)

    def dehydrate_native_place(self, student):
        return '%s%s' % (student.continent.name, student.city.name)

    def dehydrate_qq_mail(self, student):
        return '%s@qq.com' % (student.qq_number)

    def dehydrate_gender(self, student):
        return next((v for (k,v) in GENDER if k==student.gender), None)

    def dehydrate_education(self, student):
        return next((v for (k,v) in EDUCATION if k==student.education), None)
    def dehydrate_education_type(self, student):
        return next((v for (k,v) in EDUCATION_TYPE if k==student.education_type), None)
    def dehydrate_cet_level(self, student):
        return next((v for (k,v) in CET_LEVEL if k==student.cet_level), None)
    def dehydrate_registration_center(self, student):
        return next((v for (k,v) in CENTER if k==student.registration_center), None)

class SdutentExportAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    list_filter = ('class_info__name',)


admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(Student, SdutentExportAdmin)
# admin.site.register(Student, StudentAdmin)
admin.site.register(Assistant)
admin.site.register(HeadTeacher)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Continent)
admin.site.register(City)
