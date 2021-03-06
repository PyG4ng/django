from django.contrib import admin

from .models import Student, Teacher


class StudentInline(admin.TabularInline):
    model = Student.teachers.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'group']
    inlines = [StudentInline, ]
    exclude = ('teachers',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    inlines = [StudentInline, ]
