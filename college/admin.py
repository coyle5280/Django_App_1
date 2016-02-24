from django.contrib import admin
from .models import Student, Professor, Course, Section

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_id', 'start_year']

admin.site.register(Student, StudentAdmin)


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['name', 'professor_id', 'salary', 'office_number']

admin.site.register(Professor, ProfessorAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'number']

admin.site.register(Course, CourseAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'professor']

admin.site.register(Section, SectionAdmin)