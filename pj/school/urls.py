from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    
    path('detail/parent/<int:parent_id>/', views.parent_detail, name='parent_detail'),
    path('parent_add/', views.parent_add, name='parent_add'),
    path('update/parent/<int:parent_id>/', views.parent_update, name='parent_update'),
    path('delete/parent/<int:parent_id>/', views.parent_delete, name='parent_delete'),
    
    path('detail/student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('update/student/<int:student_id>/', views.student_update, name='student_update'),
    path('student_add/', views.student_add, name='student_add'),
    path('delete/student/<int:student_id>/', views.student_delete, name='student_delete'),

    path('teacher/', views.teacher, name='teacher'),
    path('teacher_add/', views.teacher_add, name='teacher_add'),
    path('update/teacher/<int:teacher_id>/', views.teacher_update, name='teacher_update'),
    path('delete/teacher/<int:teacher_id>/', views.teacher_delete, name='teacher_delete'),

    path('course/', views.course, name='course'),
    path('course_add/', views.course_add, name='course_add'),
    path('update/course/<int:course_id>/', views.course_update, name='course_update'),
    path('delete/course/<int:course_id>/', views.course_delete, name='course_delete'),

    path('school/', views.schoollist, name='schoollist'),
    path('school/checkin_add', views.checkin_add, name='checkin_add'),
    path('school/checkin_school/<int:regis_school_id>', views.checkin_school, name='checkin_school'),

    path('class/', views.classdetail, name='classdetail'),
    path('enroll/',views.enrollclass, name='enrollclass'),

    path('score/',views.studentscore, name='studentscore'),
    path('addscore/', views.scoreadd, name='scoreadd'),
    path('update/score/<int:score_id>/', views.scoreupdate, name='scoreupdate'),
    path('delete/score/<int:score_id>/', views.scoredelete, name='scoredelete'),


    path('detail/class/<int:course_id>', views.detail, name='detail'),
    path('check-in/<int:course_id>/', views.check_in, name='check_in'),
] 