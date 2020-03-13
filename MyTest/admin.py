from django.contrib import admin

# Register your models here.

from MyTest.models import Grade, Student


class GradeAdmin(admin.ModelAdmin):
    list_display = ('gname', 'gdate', 'ggirlnum', 'gboynum')
    list_filter = ('gdate', 'ggirlnum')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('sname', 'sgender', 'sgrade')
    list_filter = ('sname', 'sgender', 'sgrade')


admin.site.register(Grade, GradeAdmin)
admin.site.register(Student, StudentAdmin)
