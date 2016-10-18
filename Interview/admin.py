from django.contrib import admin

from .models import Interview, Question

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class InterviewAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]

    fields = ('company_name', 'address', 'date', 'duration', 'student', 'summary',)





admin.site.register(Interview, InterviewAdmin)
