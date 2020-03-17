# Generated by Django 3.0.4 on 2020-03-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pddusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户列表', 'verbose_name_plural': '用户列表'},
        ),
        migrations.AddField(
            model_name='userinfo',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='is_delete',
            field=models.BooleanField(default=False, help_text='逻辑删除', null=True, verbose_name='逻辑删除'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
    ]
