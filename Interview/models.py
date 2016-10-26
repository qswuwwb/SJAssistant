from django.db import models
from StudentBasic.models import Student

class Interview(models.Model):
    class Meta:
        verbose_name = "面试"
        verbose_name_plural = "面试"

    def __str__(self):
        return self.company_name

    company_name = models.CharField("公司名", max_length=20, blank=True)
    address = models.CharField("公司地址", max_length=20, blank=True)
    date = models.DateField("日期", blank=True)
    duration = models.DurationField("面试时长",  blank=True)
    student = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE)
    summary = models.TextField("面试总结", blank=True)

class Question(models.Model):
    PERFORMANCE_TYPE = (
        (1, '能流利的回答'),
        (2, '能较好的回答'),
        (3, '能勉强的回答'),
        (4, '不能回答'),
        (5, '听都没听说过'),
    )

    class Meta:
        verbose_name = "面试问题"
        verbose_name_plural = "面试问题"

    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    detail = models.CharField("问题", max_length=100)
    score = models.PositiveIntegerField("学生回答情况", choices=PERFORMANCE_TYPE, blank=True)
