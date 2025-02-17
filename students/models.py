from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from departments.models import BaseModel
from groups.models import Group
from departments.models import Department


class Gender(models.Model):
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name

class Grade(models.Model):
    grade = models.PositiveIntegerField()

    def __str__(self):
        return str(self.grade)

class Student(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='student_image/')
    enrollment_date = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='students', null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return reverse('students:detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)

class ParentGuardian(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    relationship = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='parents')

    def __str__(self):
        return f"{self.name} {self.relationship}"
