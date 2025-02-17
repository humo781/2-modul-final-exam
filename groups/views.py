from django.shortcuts import render, get_object_or_404, redirect
from departments.models import Department
from students.models import Student, Grade
from subjects.models import Subject
from teachers.models import Teacher
from .models import Group, Schedule

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/list.html', {'groups': groups})

def group_detail(request, slug):
    group = get_object_or_404(Group, slug=slug)
    student = Student.objects.all()
    ctx = {'group': group, 'student': student}
    return render(request, 'groups/detail.html', ctx)

def group_create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        academic_year = request.POST.get('academic_year')
        description = request.POST.get('description')
        max_students = request.POST.get('max_students')
        grade_level_id = request.POST.get('grade_level')

        grade_level = get_object_or_404(Grade, id=grade_level_id)

        if name and academic_year and description and max_students and grade_level:
            group = Group.objects.create(
                name=name,
                academic_year=academic_year,
                description=description,
                max_students=max_students,
                grade_level=grade_level,
            )
            subject_ids = [int(subject_id) for subject_id in request.POST.getlist('subjects') if subject_id.isdigit()]
            group.subjects.set(subject_ids)

            teacher_ids = [int(teacher_id) for teacher_id in request.POST.getlist('teachers') if teacher_id.isdigit()]
            group.teachers.set(teacher_ids)

            return redirect('groups:list')

    grades = Grade.objects.all()
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    schedules = Schedule.objects.all()
    ctx = {'grades': grades,
           'subjects': subjects,
           'teachers': teachers,
           'schedules': schedules}
    return render(request, 'groups/form.html', ctx)

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':

        name = request.POST.get('name')
        academic_year = request.POST.get('academic_year')
        description = request.POST.get('description')
        max_students = request.POST.get('max_students')
        grade_level_id = request.POST.get('grade_level')

        grade = get_object_or_404(Grade, id=grade_level_id)

        if name and academic_year and description and max_students and grade:
            group.name = name
            group.academic_year = academic_year
            group.description = description
            group.max_students = max_students
            group.grade_level = grade.id

            subject_ids = [int(subject_id) for subject_id in request.POST.getlist('subjects') if subject_id.isdigit()]
            group.subjects.set(subject_ids)

            teacher_ids = [int(teacher_id) for teacher_id in request.POST.getlist('teachers') if teacher_id.isdigit()]
            group.teachers.set(teacher_ids)

            group.save()
            return redirect(group.get_detail_url())

    grades = Grade.objects.all()
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    schedules = Schedule.objects.all()
    ctx = {'group': group,
           'grades': grades,
           'subjects': subjects,
           'teachers': teachers,
           'schedules': schedules}
    return render(request, 'groups/form.html', ctx)

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('groups:list')
    return render(request, 'groups/delete.html', {'group': group})


