from django.db import models

# Create your models here.


class Grade(models.Model):
    # 班级名称
    gname = models.CharField(verbose_name="班级名称", max_length=10)

    # 开班日期
    gdate = models.DateTimeField(verbose_name="开班日期")

    # 女生数量
    ggirlnum = models.IntegerField(verbose_name="女生数量")

    # 男生数量
    gboynum = models.IntegerField(verbose_name="男生数量")

    # 是否已逻辑删除
    isDelete = models.BooleanField(verbose_name="删除")

    class Meta:
        verbose_name = "班级信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.gname


class Student(models.Model):

    GENDER = (
        (0, "女"),
        (1, "男")
    )

    # 学生姓名
    sname = models.CharField(verbose_name="学生姓名", max_length=20)

    # 学生性别
    sgender = models.BooleanField(verbose_name="学生性别", choices=GENDER, default=True)

    # 学生年龄
    sage = models.IntegerField(verbose_name="学生年龄")

    # 备注信息
    sinfo = models.CharField(verbose_name="备注信息", max_length=64)

    # 是否逻辑删除
    isDelete = models.BooleanField(verbose_name="删除", default=False)

    # 学生所属班级
    sgrade = models.ForeignKey(Grade, verbose_name="学生所属班级", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "学生信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sname
