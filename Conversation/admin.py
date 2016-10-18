from django.contrib import admin

from .models import Conversation

class ConversationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['student', 'time', 'operator']}),
        ('评分', {'fields': ['deportment_score', 'deportment_problem',
                           'expression_score', 'expression_problem',
                           'resume_score', 'resume_problem',
                           'background_score', 'background_problem',
                           'project_score', 'project_problem',
                           'skill_point_score', 'skill_point_problem',
                           'mentality_score', 'mentality_problem',
                           ]}),
        ('总结', {'fields': ['task', 'task_completion']}),
    ]

    list_display = ('student', 'time')
    list_filter = ['time', 'student']
    # search_fields = ['student', 'time']


admin.site.register(Conversation, ConversationAdmin)
