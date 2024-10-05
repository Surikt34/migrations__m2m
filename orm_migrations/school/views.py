from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # Извлекаем всех студентов и сортируем по группе
    students = Student.objects.all().order_by('group')
    # print(students)
    context = {
        'object_list': students,
    }

    return render(request, template, context)
