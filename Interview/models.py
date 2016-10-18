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
    date = models.DateField("日期")
    duration = models.DurationField("面试时长")
    student = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE)
    summary = models.TextField("面试总结")

class Question(models.Model):

    class Meta:
        verbose_name = "面试问题"
        verbose_name_plural = "面试问题"

    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    detail = models.CharField("详情", max_length=100)
