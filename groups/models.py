from django.db import models
from django.urls import reverse
from departments.models import BaseModel
from teachers.models import Teacher

class Schedule(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Group(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    academic_year = models.CharField(max_length=100)
    description = models.TextField()
    max_students = models.PositiveIntegerField()
    grade_level = models.PositiveIntegerField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='groups', default=2)
    teachers = models.ManyToManyField(Teacher, related_name='groups')
    subjects = models.ManyToManyField('subjects.Subject', related_name='groups')

    def __str__(self):
        return self.name

    def get_detail_url(self):
        return reverse('groups:detail', args=[self.slug])
