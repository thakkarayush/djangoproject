from django import forms


class CourseEntryForm(forms.Form):
    name=forms.CharField(max_length=30)
    address=forms.CharField(max_length=50)
    std=forms.IntegerField()
    rollno=forms.IntegerField()