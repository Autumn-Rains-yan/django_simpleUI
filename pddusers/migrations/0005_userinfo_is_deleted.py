# Generated by Django 3.0.4 on 2020-03-17 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pddusers', '0004_remove_userinfo_is_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
