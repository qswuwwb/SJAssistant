from django.db import models
from StudentBasic.models import Student

class Conversation(models.Model):
    class Meta:
        verbose_name = "访谈"
        verbose_name_plural = "访谈"

    # def __str__(self):
    #     return "第%d次访谈%s" % (self.id, self.time.strftime('%Y-%m-%d'))

    OPERATOR = (
        ('YinSJ', '尹胜杰'),
        ('GuoQH', '郭巧会'),
        ('JinNa', '金娜'),
    )

    RANK = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    time = models.DateTimeField("访谈时间")

    operator = models.CharField("访谈人", choices=OPERATOR, max_length=10)
    student = models.ForeignKey(Student, verbose_name="学生", on_delete=models.CASCADE)

    deportment_score = models.PositiveIntegerField("仪态", choices=RANK, help_text='哈哈，SB', default=1)
    deportment_problem = models.CharField("存在的问题", max_length=50, blank=True, default="")

    expression_score = models.PositiveIntegerField("表达", choices=RANK, default=1)
    expression_problem = models.CharField("存在的问题",max_length=50, blank=True, default="")

    resume_score = models.PositiveIntegerField("简历", choices=RANK, default=1)
    resume_problem = models.CharField("存在的问题",max_length=50, blank=True, default="")

    background_score = models.PositiveIntegerField("背景", choices=RANK, default=1)
    background_problem = models.CharField("存在的问题",max_length=50, blank=True, default="")

    project_score = models.PositiveIntegerField("项目", choices=RANK, default=1)
    project_problem = models.CharField("存在的问题",max_length=50, blank=True, default="")

    skill_point_score = models.PositiveIntegerField("技能", choices=RANK, default=1)
    skill_point_problem = models.CharField("存在的问题",max_length=50, blank=True, default="")

    mentality_score = models.PositiveIntegerField("心态", choices=RANK, default=1)
    mentality_problem = models.CharField("存在的问题",max_length=50, blank=True, default="")

    task = models.TextField("要求")
    task_completion = models.TextField("评语", blank=True, default="")

