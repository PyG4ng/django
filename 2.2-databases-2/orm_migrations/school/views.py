from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list_view(request):
    ordering = 'group'
    template = 'school/students_list.html'
    students = Student.objects.all().order_by(ordering).prefetch_related('teachers')
    context = {
        'object_list': students
    }
    return render(request, template, context)
