from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey
import time
from django.core import validators

GENDER = (
        ('M', '男'),
        ('F', '女'),
    )

EDUCATION = (
        ('junior', '初中及以下'),
        ('high', '高中'),
        ('secondary', '中专'),
        ('college', '大专'),
        ('university', '本科'),
        ('master', '硕士及以上'),
)

EDUCATION_TYPE = (
    ('1','全日制统招'),
    ('2','函授'),
    ('3','自考'),
    ('4','其他'),
)

CET_LEVEL = (
    ('1','英语四级'),
    ('2','英语六级'),
    ('3','其他'),
    ('4','无'),
)

CENTER = (
    ('szlg', '深圳龙岗中心'),
    ('szba', '深圳宝安中心'),
    ('szbt', '深圳宝体中心'),
    ('szkjy', '深圳科技园中心'),
    ('szlh', '深圳罗湖中心'),
    ('szdw', '深圳地王中心'),
    ('szsd', '深圳深大中心'),
    ('szlhua', '深圳龙华中心'),
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
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class HeadTeacher(models.Model):
    class Meta:
        verbose_name = "班主任"
        verbose_name_plural = "班主任"
    name = models.CharField("姓名", max_length=10)
    entry_time = models.DateField("入职日期", null=True)
    phone_number = models.CharField("手机号", max_length=11, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

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


class Continent(models.Model):
    name = models.CharField('省', max_length=255)
    def __str__(self):
        return self.name

class City(models.Model):

    class Meta:
        verbose_name = "市"
        verbose_name_plural = "市"

    continent = models.ForeignKey(Continent)
    name = models.CharField('市', max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):

    class Meta:
        verbose_name = "学员信息"
        verbose_name_plural = "学员信息"

    id_number_validator = validators.RegexValidator(regex=r'^\d{17}[\d,x,X]', message='请输入正确的身份证号')
    phone_number_validator = validators.RegexValidator(regex=r'^\d{11}', message='请输入正确的手机号')

    name = models.CharField("姓名", max_length=10)
    gender = models.CharField("性别", max_length=1, choices=GENDER)
    id_number = models.CharField("身份证号", max_length=18, validators=[id_number_validator])

    phone_number = models.CharField("手机号", max_length=11, validators=[phone_number_validator])
    qq_number = models.CharField("QQ号", max_length=20)
    contact = models.CharField("紧急联系人", max_length=10)
    contact_phone = models.CharField("紧急联系人手机号", max_length=20)
    continent = models.ForeignKey(Continent, verbose_name="省")
    city = ChainedForeignKey(
        City,
        chained_field="continent",
        chained_model_field="continent",
        show_all=False,
        auto_choose=True,
        sort=True,
    )

    graduated_school = models.CharField("毕业学校", max_length=20, null=True)
    education = models.CharField("学历", max_length=10, choices=EDUCATION)
    education_type = models.CharField("学历性质", max_length=1, choices=EDUCATION_TYPE)
    cet_level = models.CharField("英语四六级", max_length=1, choices=CET_LEVEL)
    discipline = models.CharField("专业", max_length=100, blank=True)
    graduated_date = models.DateField("毕业时间", help_text='格式如2015-09-01')

    registration_center = models.CharField("报名中心", max_length=10, choices=CENTER)
    class_info = models.ForeignKey(ClassInfo, verbose_name="班级", on_delete=models.CASCADE)

    # @classmethod
    def birthday(self):
        birthday = time.strptime(self.id_number[6:14], '%Y%m%d')
        return time.strftime('%Y年%m月%d日', birthday)
    def __str__(self):
        return self.name



