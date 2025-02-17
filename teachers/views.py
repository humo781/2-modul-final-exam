from django.shortcuts import render, get_object_or_404, redirect
from departments.models import Department
from groups.models import Group
from students.models import Student
from subjects.models import Subject
from .models import Teacher, EmploymentType


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/list.html', {'teachers': teachers})

def teacher_detail(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    group = Group.objects.all()
    student = Student.objects.all()
    ctx = {'teacher': teacher, 'group': group, 'student': student}
    return render(request, 'teachers/detail.html', ctx)

def teacher_create(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        department_id = request.POST.get('department')
        qualification = request.POST.get('qualification')
        image = request.FILES.get('image')
        employment_type = request.POST.get('employment_type')

        department = get_object_or_404(Department, id=department_id)

        if (first_name and last_name and address and phone_number and email and department and image and
                qualification and employment_type):
            teacher = Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone_number=phone_number,
                email=email,
                department=department,
                qualification=qualification,
                image=image,
                # join_date=join_date,
                employment_type=employment_type,
            )
            subject_ids = [int(subject_id) for subject_id in request.POST.getlist('subjects') if subject_id.isdigit()]
            teacher.subject.set(subject_ids)
            return redirect('teachers:list')

    departments = Department.objects.all()
    subjects = Subject.objects.all()
    employments = EmploymentType.objects.all()
    ctx = {'departments': departments, 'subjects': subjects, 'employments': employments}
    return render(request, 'teachers/form.html', ctx)

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        department_id = request.POST.get('department')
        qualification = request.POST.get('qualification')
        image = request.FILES.get('image')
        employment_type_id = request.POST.get('employment_type')

        department = get_object_or_404(Department, id=department_id)
        employment_type = get_object_or_404(EmploymentType, id=employment_type_id)

        if (first_name and last_name and address and phone_number and email and department and image and
                qualification and employment_type):
            teacher.first_name = first_name
            teacher.last_name = last_name
            teacher.address = address
            teacher.phone_number = phone_number
            teacher.email = email
            teacher.department = department
            teacher.image = image
            teacher.qualification = qualification
            teacher.employment_type = employment_type
            teacher.save()
            return redirect(teacher.get_detail_url())

    departments = Department.objects.all()
    subjects = Subject.objects.all()
    employments = EmploymentType.objects.all()
    ctx = {'teacher': teacher, 'departments': departments, 'subjects': subjects, 'employments': employments}
    return render(request, 'teachers/form.html', ctx)

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers:list')
    return render(request, 'teachers/delete.html', {'teacher': teacher})


