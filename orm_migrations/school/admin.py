from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group', 'get_teachers')  # Отображаем имя, класс и учителей
    search_fields = ('name', 'group')  # Поля для поиска
    list_filter = ('group',)  # Фильтр по классам
    filter_horizontal = ('teachers',)  # Удобный виджет для ManyToMany поля

    def get_teachers(self, obj):
        """Функция для отображения всех учителей в списке студентов"""
        return ", ".join([teacher.name for teacher in obj.teachers.all()])

    get_teachers.short_description = 'Учителя'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')  # Отображаем имя и предмет учителя
    search_fields = ('name', 'subject')  # Поля для поиска
