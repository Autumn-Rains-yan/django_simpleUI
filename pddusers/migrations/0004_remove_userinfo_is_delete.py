# Generated by Django 3.0.4 on 2020-03-17 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pddusers', '0003_auto_20200317_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='is_delete',
        ),
    ]
