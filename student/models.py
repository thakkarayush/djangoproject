from django.db import models
from django.urls import reverse

# Create your models here.
class student_master(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    address=models.TextField()
    std=models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.rollno}"

    def get_absolute_url(self):
        return reverse('student-view')