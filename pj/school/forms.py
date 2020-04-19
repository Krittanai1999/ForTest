from django import forms
from django.forms.widgets import CheckboxSelectMultiple


from .models import Teacher, Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
       
        fields = ('name', 'course_id', 'room', 'weekday', 'capacity', 'start_time', 'end_time', 'teach_course')
        labels = {
            'name': 'COURSE',
            'course_id': 'COURSE ID',
            'room': 'ROOM',
            'weekday': 'DAY',
            'capacity': 'CAPACITY',
            'start_time': 'START TIME',
            'end_time': 'END TIME',
            'teach_course': 'TEACHER'
        }
        widgets = {
             "teach_course":CheckboxSelectMultiple(),
             'title': forms.TextInput(attrs={ 'class' : 'form-control' },)
        }