from django.shortcuts import render, get_object_or_404, redirect
from departments.models import Department
from students.models import Student, Grade
from teachers.models import Teacher
from .models import Subject

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/list.html', {'subjects': subjects})

def subject_detail(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    return render(request, 'subjects/detail.html', {'subject': subject})

def subject_create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        credit_hours = request.POST.get('credit_hours')
        grade_id = request.POST.get('grade')

        grade = get_object_or_404(Grade, id=grade_id)

        if name and description and credit_hours and grade:
            subject = Subject.objects.create(
                name=name,
                description=description,
                credit_hours=credit_hours,
                grade=grade,
            )

            department_ids = [int(department_id) for department_id in request.POST.getlist('department')
                              if department_id.isdigit()]
            subject.department.set(department_ids)

            return redirect('subjects:list')

    grades = Grade.objects.all()
    departments = Department.objects.all()

    ctx = {'grades': grades,
           'departments': departments,
           }
    return render(request, 'subjects/form.html', ctx)

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':

        name = request.POST.get('name')
        description = request.POST.get('description')
        credit_hours = request.POST.get('credit_hours')
        grade_id = request.POST.get('grade')
        department_id = request.POST.get('department')

        grade = get_object_or_404(Grade, id=grade_id)
        department = get_object_or_404(Department, id=department_id)

        if name and description and credit_hours and grade and department:
            subject.name = name
            subject.credit_hours = credit_hours
            subject.description = description
            subject.grade = grade
            subject.department = department
            subject.save()
            return redirect(subject.get_detail_url())

    grades = Grade.objects.all()
    departments = Department.objects.all()

    ctx = {'grades': grades,
           'subject': subject,
           'departments': departments
           }
    return render(request, 'subjects/form.html', ctx)

def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subjects:list')
    return render(request, 'subjects/delete.html', {'subject': subject})


