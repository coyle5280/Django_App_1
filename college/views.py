from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from college.models import Student
from college.models import Course
from college.models import Professor

from college.forms import StudentForm
from college.forms import ProfessorForm
from college.forms import CourseForm

from django.http import Http404


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def student(request):
    list_off_students = Student.objects.all()
    context = {'student_List': list_off_students}
    return render(request, 'student/student.html', context)


@login_required
def student_detail(request, id):
    try:
        student_info = Student.objects.get(id=id)
    except Student.DoesNotExist:
        raise Http404('This student does not exist')
    return render(request, 'student/student_detail.html', {
        'student': student_info
    })


@login_required
def new_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            StudentForm.save(form)
            return redirect('student')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form': form})


@login_required
def professor(request):
    professor_list = Professor.objects.all()
    context = {'professor_List': professor_list}
    return render(request, 'professor/professor.html', context)


@login_required
def professor_update(request):
    professor_list = Professor.objects.all()
    context = {'professor_List': professor_list}
    return render(request, 'professor/professor.html', context)


@login_required
def professor_detail(request, id):
    try:
        professor_object = Professor.objects.get(id=id)
    except Professor.DoesNotExist:
        raise Http404('This professor does not exist')
    return render(request, 'professor/professor_detail.html', {
        'professor': professor_object})


@login_required
def course(request):
    course_list = Course.objects.all()
    context = {'courseList': course_list}
    return render(request, 'course/course.html', context)


@login_required
def course_detail(request, id):
    try:
        course_object = Course.objects.get(id=id)
    except Course.DoesNotExist:
        raise Http404('This course does not exist')
    return render(request, 'course/course_detail.html', {
        'course': course_object})


@login_required
def new_professor(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            ProfessorForm.save(form)
            return redirect('professor')
    else:
        form = ProfessorForm()
    return render(request, 'professor/professor_form.html', {'form': form})


@login_required
def new_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            CourseForm.save(form)
            return redirect('course')
    else:
        form = ProfessorForm()
    return render(request, 'course/course_form.html', {'form': form})