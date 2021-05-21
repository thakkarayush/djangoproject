from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from django.shortcuts import render,redirect
from .models import student_master
from .form import CourseEntryForm

class StudentEntryView(CreateView):
    model = student_master
    fields = '__all__'
    template_name = 'student/student_register.html'

class StudentListView(ListView):
    model = student_master
    template_name = 'student/student_view.html'
    context_object_name = 'students'
    ordering = ['-name']

class StudentUpdateView(UpdateView):
    model = student_master
    fields = '__all__'
    template_name = 'student/student_register.html'
    #if we do not give template name it will be looking for student_master_detail.html

class StudentDetailView(DetailView):
    model = student_master
    #student_master_detail.html

class StudentDeleteView(DeleteView):
    model = student_master
    #student_master_confirm_delete.html
    success_url = '/student/view'
