from django.urls import path

from school.views import students_list_view

urlpatterns = [
    path('', students_list_view, name='students'),
]
