from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Parent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    relation = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    workplace = models.TextField(null=True) #อาชีพ
    income = models.IntegerField(null=True)
    address = models.TextField()
    type_of_house = models.CharField(max_length=255)

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=12)
    room = models.CharField(max_length=255)
    teacher_user_id = models.CharField(max_length=6) 
    image = models.ImageField(upload_to='uploads/', null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Course(models.Model):
    name = models.CharField(max_length=255)
    course_id = models.CharField(max_length=8)
    room = models.CharField(max_length=4, null=True)
    WEEKDAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    weekday = models.CharField(max_length=255, choices=WEEKDAYS, null=False)
    capacity = models.SmallIntegerField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    teach_course = models.ManyToManyField(Teacher)

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_of_birth = models.CharField(max_length=10)
    age = models.SmallIntegerField()
    phone_number = models.CharField(max_length=12)
    address = models.TextField()
    GENDERS = (
        ('M', 'Male'),
        ('Fe', 'Female')
    )
    gender = models.CharField(max_length=2, choices=GENDERS)
    class_room = models.CharField(max_length=6)
    stu_no = models.SmallIntegerField()
    track = models.CharField(max_length=25)
    student_user_id = models.CharField(max_length=5,  null=True) 
    parent_id = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

class Regis_school(models.Model):
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    check_type =  models.BooleanField()
    score = models.SmallIntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Enroll(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)

class Attendance(models.Model):
    score = models.SmallIntegerField()
    score_percent = models.SmallIntegerField()
    session = models.SmallIntegerField()
    enroll = models.ForeignKey(Enroll, on_delete=models.CASCADE)