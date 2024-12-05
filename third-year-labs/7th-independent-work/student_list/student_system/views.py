from django.shortcuts import render, redirect
from .forms import StudentForm, GradeForm
from .models import Student, Grade


def student_list(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        grade_form = GradeForm(request.POST)
        if student_form.is_valid() and grade_form.is_valid():
            student = student_form.save()
            grade = grade_form.save(commit=False)
            grade.student = student
            grade.save()
            return redirect('student_list')
    else:
        student_form = StudentForm()
        grade_form = GradeForm()

    students = Student.objects.all()
    grades = Grade.objects.all()
    return render(request, 'students/base.html', {
        'student_form': student_form,
        'grade_form': grade_form,
        'students': students,
        'grades': grades
    })
