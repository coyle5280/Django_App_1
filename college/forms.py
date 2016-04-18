from django import forms
from django.forms import ModelForm

from college.models import Student
from college.models import Professor
from college.models import Course
from college.models import Section

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'start_year']


class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['professor_id', 'name', 'office_number', 'salary']


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'number', 'department']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'course', 'professor']