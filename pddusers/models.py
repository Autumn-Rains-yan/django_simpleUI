from django.db import models

# Create your models here.
from services.django_softdelete_model import SoftDeleteModel


class UserInfo(SoftDeleteModel):

    class Meta:
        verbose_name = "用户列表"
        verbose_name_plural = verbose_name

    user_name = models.CharField(verbose_name='用户名', max_length=64)
    password = models.CharField(verbose_name='密码', max_length=64)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True, null=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True)
