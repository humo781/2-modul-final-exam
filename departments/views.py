from django.shortcuts import render, get_object_or_404, redirect

from groups.models import Group
from students.models import Student
from subjects.models import Subject
from .models import Department
from teachers.models import Teacher

def dashboard(request):
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    subject = Subject.objects.all()
    group = Group.objects.filter(status=True)
    print(group)
    ctx = {'student': student,
           'teacher': teacher,
           'subject': subject,
           'group': group}
    return render(request, 'dashboard.html', ctx)

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/list.html', {'departments': departments})

def department_detail(request, slug):
    department = get_object_or_404(Department, slug=slug)
    active_subjects = department.subjects.filter(status=True).count()
    ctx = {'department': department, 'subjects': active_subjects}
    return render(request, 'departments/detail.html', ctx)

def department_create(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        head_id = request.POST.get('head')
        desc = request.POST.get('desc')
        location = request.POST.get('location')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')

        head = Teacher.objects.get(id=head_id)

        if name and head and desc and location and contact_email and contact_phone:
            Department.objects.create(
                name=name,
                head_of_department=head,
                description=desc,
                location=location,
                contact_email=contact_email,
                contact_phone=contact_phone
            )
            return redirect('departments:list')
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'departments/form.html', ctx)

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':

        name = request.POST.get('name')
        head_id = request.POST.get('head')
        desc = request.POST.get('desc')
        location = request.POST.get('location')
        contact_email = request.POST.get('contact_email')
        contact_phone = request.POST.get('contact_phone')

        head = get_object_or_404(Teacher, pk=head_id)
        if name and head and desc and location and contact_email and contact_phone:

            department.name = name
            department.head_of_department = head
            department.description = desc
            department.location = location
            department.contact_email = contact_email
            department.contact_phone = contact_phone
            department.save()
            return redirect(department.get_detail_url())

    teachers = Teacher.objects.all()
    ctx = {'department': department, 'teachers': teachers}
    return render(request, 'departments/form.html', ctx)

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('departments:list')
    return render(request, 'departments/delete.html', {'department': department})


