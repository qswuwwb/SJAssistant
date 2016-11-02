from django.db import models
from StudentBasic.models import Student, Assistant
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone as timezone

DISCIPLINE_TYPE = (
    ('absenteeism', '旷课'),
    ('late', '迟到'),
    ('early_retirement', '早退'),
    ('sleep', '打瞌睡'),
    ('play_phone', '玩手机'),
    ('play_game', '玩游戏'),
    ('watch_video', '看电影/视频'),
    ('other', '其他'),
)
class StudentDiscipline(models.Model):
    class Meta:
        verbose_name = "考勤纪律"
        verbose_name_plural = "考勤纪律"

    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models = models.PositiveIntegerField()
    # operator = GenericForeignKey('content_type', 'object_id')
    operator = models.ForeignKey(User, verbose_name='操作人', null=True, editable=False)
    add_date = models.DateTimeField(editable=False, default=timezone.now)
    type = models.CharField('考勤违纪类型', max_length=20, choices=DISCIPLINE_TYPE, null=True)
    description = models.CharField('描述', max_length=50, null=True)
    student = models.ForeignKey(Student, verbose_name='学生', null=True)


    def __str__(self):
        return self.student.name
