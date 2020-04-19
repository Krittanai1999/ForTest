# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Permission
from school.models import Parent, Teacher, Course, Student, Regis_school, Enroll, Attendance, Score, StudentAttendance

admin.site.register(Permission)

class ParentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    list_per_page = 10
admin.site.register(Parent, ParentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name']
    list_per_page = 10
admin.site.register(Teacher, TeacherAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course_id']
    list_per_page = 10
admin.site.register(Course, CourseAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name']
    list_per_page = 10
admin.site.register(Student, StudentAdmin)

class Regis_schoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'datetime', 'check_type']
    list_per_page = 10
admin.site.register(Regis_school, Regis_schoolAdmin)

class EnrollAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course']
    list_per_page = 10
admin.site.register(Enroll, EnrollAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'datetime', 'check_type', 'enroll']
    list_per_page = 10
admin.site.register(Attendance, AttendanceAdmin)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'point', 'check_type']
    list_per_page = 10
admin.site.register(Score, ScoreAdmin)



class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'classroom', 'attend', 'timestamp']
    list_per_page = 10

admin.site.register(StudentAttendance, StudentAttendanceAdmin)