from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from departments.models import BaseModel, Department

class EmploymentType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Teacher(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='teacher_images/')
    slug = models.SlugField(unique=True, blank=True, null=True)
    qualification = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
    join_date = models.DateField(auto_now_add=True)
    employment_type = models.OneToOneField(EmploymentType, on_delete=models.CASCADE, related_name='teachers')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')
    subject = models.ManyToManyField('subjects.Subject', related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_detail_url(self):
        return reverse('teachers:detail', args=[
            self.slug
        ])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        super().save(*args, **kwargs)
