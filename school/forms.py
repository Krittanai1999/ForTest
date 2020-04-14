from django import forms
from django.forms.widgets import CheckboxSelectMultiple


from .models import Teacher, Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
       
        fields = ('name', 'course_id', 'room', 'weekday', 'capacity', 'start_time', 'end_time', 'teach_course')
        labels = {
            'name': 'ชื่อวิชา',
            'course_id': 'รหัสวิชา',
            'room': 'ห้องเรียน',
            'weekday': 'วันที่เรียน',
            'capacity': 'จำนวนที่รับ',
            'start_time': 'เวลาเริ่ม',
            'end_time': 'เวลาสิ้นสุด',
            'teach_course': 'ครูผู้สอน'
        }
        widgets = {
             "teach_course":CheckboxSelectMultiple(),
             'title': forms.TextInput(attrs={ 'class' : 'form-control' },)
        }