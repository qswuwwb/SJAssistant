from django.db import models
from django.contrib.auth.models import User

GENDER = (
        ('M', '男'),
        ('F', '女'),
    )

EDUCATION = (
        ('junior', '初中及以下,我的爷啊'),
        ('high', '高中'),
        ('secondary', '中专'),
        ('college', '大专'),
        ('university', '本科'),
        ('master', '硕士及以上，我的哥啊'),
)


class Assistant(models.Model):
    class Meta:
        verbose_name = "项目经理信息"
        verbose_name_plural = "项目经理信息"
    name = models.CharField("姓名", max_length=10)
    entry_time = models.DateField("入职日期", null=True)
    phone_number = models.CharField("手机号", max_length=11, null=True)
    education = models.CharField("学历", max_length=10, choices=EDUCATION)
    graduated_school = models.CharField("毕业学校", max_length=20, null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class HeadTeacher(models.Model):
    class Meta:
        verbose_name = "班主任"
        verbose_name_plural = "班主任"
    name = models.CharField("姓名", max_length=10)
    entry_time = models.DateField("入职日期", null=True)
    phone_number = models.CharField("手机号", max_length=11, null=True)

    def __str__(self):
        return self.name
class ClassInfo(models.Model):

    class Meta:
        verbose_name = "班级信息"
        verbose_name_plural = "班级信息"

    PRODUCT = (
        ('iOS', 'iOS'),
        ('PHP', 'PHP'),
        ('Java', 'Java')
    )

    name = models.CharField("班级名", max_length=10)
    product = models.CharField("产品线", max_length=4, choices=PRODUCT)
    assistant = models.ForeignKey(Assistant, verbose_name="项目经理", on_delete=models.CASCADE)
    head_teacher = models.ForeignKey(HeadTeacher, verbose_name="班主任", on_delete=models.CASCADE)
    graduated_date = models.DateField("结课时间")

    def __str__(self):
        return self.name

class Student(models.Model):

    class Meta:
        verbose_name = "学员信息"
        verbose_name_plural = "学员信息"


    name = models.CharField("姓名", max_length=10)
    gender = models.CharField("性别", max_length=1, choices=GENDER)
    birthday = models.DateField("生日")
    phone_number = models.CharField("手机号", max_length=11, null=True)
    education = models.CharField("学历", max_length=10, choices=EDUCATION)
    graduated_school = models.CharField("毕业学校", max_length=20, null=True)
    class_info = models.ForeignKey(ClassInfo, verbose_name="班级", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
