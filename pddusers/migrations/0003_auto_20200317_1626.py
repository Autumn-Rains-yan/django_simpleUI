# Generated by Django 3.0.4 on 2020-03-17 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pddusers', '0002_auto_20200317_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='is_delete',
            field=models.BooleanField(default=False, help_text='逻辑删除', verbose_name='逻辑删除'),
        ),
    ]