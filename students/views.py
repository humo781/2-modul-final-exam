from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, ParentGuardian, Gender, Grade
from groups.models import Group
from departments.models import Department

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def student_detail(request, slug):
    student = get_object_or_404(Student, slug=slug)
    ctx = {'student': student}
    return render(request, 'students/detail.html', ctx)

def student_create(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        grade = request.POST.get('grade')
        gender_id = request.POST.get('gender')
        dob = request.POST.get('dob')
        image = request.FILES.get('image')
        group_id = request.POST.get('group')
        # department_id = request.POST.get('department')

        group = get_object_or_404(Group, id=group_id)
        gender = get_object_or_404(Gender, id=gender_id)
        # department = Department.objects.get(id=department_id)

        if (first_name and last_name and address and phone_number and email and grade and dob and image and
                gender and group):
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                address=address,
                phone_number=phone_number,
                email=email,
                grade=grade,
                dob=dob,
                image=image,
                gender=gender,
                group=group,
                # department=department
            )
            return redirect('students:list')

    groups = Group.objects.all()
    genders = Gender.objects.all()
    grades = Grade.objects.all()
    ctx = {'groups': groups, 'genders': genders, 'grades': grades}
    return render(request, 'students/form.html', ctx)

# def parent_guardian_create(request):
#
#     if request.method == 'POST':
#         parent_g_name = request.POST.get('p/g name')
#         parent_g_phone = request.POST.get('p/g phone')
#         parent_g_email = request.POST.get('p/g email')
#
#         if parent_g_name and parent_g_email and parent_g_phone:
#             ParentGuardian.objects.create(
#                 name=parent_g_name,
#                 email=parent_g_email,
#                 phone_number=parent_g_phone
#             )
#             return redirect('students:list')
#     return render(request, 'students/form.html')

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        image = request.POST.get('image')
        group_id = request.POST.get('group')
        department_id = request.POST.get('department')

        group = Group.objects.get(id=group_id)
        department = Department.objects.get(id=department_id)

        if (first_name and last_name and address and phone_number and email and dob and image
                and group and department):
            student.first_name = first_name,
            student.last_name = last_name,
            student.address = address,
            student.phone_number = phone_number,
            student.email = email,
            student.dob = dob,
            student.image = image,
            student.group = group,
            student.department = department
            student.save()
            return redirect(student.get_detail_url())

    groups = Group.objects.all()
    genders = Gender.objects.all()
    grades = Grade.objects.all()
    ctx = {'student': student, 'groups': groups, 'genders': genders, 'grades': grades}
    return render(request, 'students/form.html', ctx)

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students:list')
    return render(request, 'students/delete.html', {'student': student})


