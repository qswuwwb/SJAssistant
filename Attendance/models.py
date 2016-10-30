from django.db import models
from StudentBasic.models import Assistant
class Attendance(models.Model):
    TYPE = (
        ('overtime_day', '加班一天'),
        ('overtime_night', '加班一晚'),
        ('overtime_onduty', '夜晚值班'),
        ('leave', '请假一天'),
    )
    class Meta:
        verbose_name = "加班与请假"
        verbose_name_plural = "加班与请假"
 
    assistant = models.ForeignKey(Assistant, verbose_name="项目经理", null=True)
    type = models.CharField("加班/请假类型", choices=TYPE, max_length=20, null=True)
    date = models.DateField("日期", null=True)
    reason = models.CharField("加班原因", max_length=50, null=True)
    # weekAttendance = models.ForeignKey(WeekAttendance, verbose_name="周提交")

# class WeekAttendance(models.Model):
#     class Meta:
#         verbose_name = "周工作提交"
