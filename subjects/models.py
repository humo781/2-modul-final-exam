from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from departments.models import BaseModel
from departments.models import Department
from students.models import Grade
from students.models import Student

class Subject(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    credit_hours = models.PositiveIntegerField()
    grade = models.OneToOneField(Grade, on_delete=models.CASCADE, related_name='subjects')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects', default=1)
    student = models.ManyToManyField(Student, related_name='subjects')
    prerequisites = models.ManyToManyField('self', blank=True, null=True, symmetrical=False, related_name='subjects')

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('subjects:detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
