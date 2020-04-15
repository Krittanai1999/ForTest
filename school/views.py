from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.contrib.auth.models import Group, User
from django.shortcuts import get_list_or_404, get_object_or_404

from school.models import Student, Parent, Teacher, Course, Regis_school, Enroll, Attendance
from school.forms import CourseForm


def my_login(request):
    context = {}

    if request.method == 'POST': 
        username = request.POST.get('username') 
        password = request.POST.get('password') 

        user = authenticate(request, username=username, password=password) 

        if user: 
            login(request, user) 

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name='login.html', context=context)

def my_logout(request):
    logout(request)
    return redirect('login')

def index(request):
    
    print(request.user)
    user = User.objects.all()
    student = Student.objects.all()
    parent = Parent.objects.all()
    search = request.GET.get('search', '')
    context ={}
    students = User.objects.filter(
        Q(first_name__icontains=search) | 
        Q(last_name__icontains=search) | 
        Q(username__icontains=search)
    ).order_by('username')
   
    return render(request, 'index.html', context={
        'student': student,
        'parent' : parent,
        'user': user
    })

def parent_detail(request, parent_id):
   
    parent = Parent.objects.get(pk=parent_id)
   
    return render(request, 'parent/parentdetail.html', context={
        'parent': parent
        
    })

def parent_add(request):
  
    parent = Parent.objects.all()
    msg = ''
    if request.method == 'POST':
        parent = Parent.objects.create(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            relation = request.POST.get('relation'),
            workplace = request.POST.get('workplace'),
            income = request.POST.get('income'),
            phone_number = request.POST.get('phone_number'),
            email = request.POST.get('email'),
            address = request.POST.get('address'),
            type_of_house = request.POST.get('type_of_house'),
            
        )
        msg = 'SUCCESSFULLY ADD NEW PARENT NAME : %s' % (parent.first_name)
    else:
        
        parent = Parent.objects.none()
    context = {
        'parent': parent,
        'msg': msg
    }

    return render(request, 'parent/parent_add.html', context=context)

def parent_update(request, parent_id):
    
    try:
        parent = Parent.objects.get(pk=parent_id)
        msg = ''
    except parent.DoesNotExist: 
        return redirect('index')

    if request.method == 'POST':
        parent.first_name=request.POST.get('first_name')
        parent.last_name=request.POST.get('last_name')
        parent.relation=request.POST.get('relation')
        parent.workplace=request.POST.get('workplace')
        parent.income=request.POST.get('income')
        parent.phone_number=request.POST.get('phone_number')
        parent.email=request.POST.get('email')
        parent.address=request.POST.get('address')
        parent.type_of_house=request.POST.get('type_of_house')

        parent.save()
        msg = 'SUCCESSFULLY UPDATE PARENT NAME : %s' % (parent.first_name)
    
    context = {
        'parent': parent,    
        'msg': msg
    }

    return render(request, 'parent/parent_add.html', context=context)

def parent_delete(request, parent_id):
    
    parent = Parent.objects.get(id = parent_id)
    parent.delete()
    return redirect(to='index')

def student_add(request):
   
    student = Student.objects.all()
    parent = Parent.objects.all()
    teacher = Teacher.objects.all()
    msg = ''

    if request.method == 'POST':
        
        user = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'),
            '1234',
            
        )
        group = Group.objects.get(name='student')
        user.groups.add(group)
        user.save()
        
        
        # birthday = request.POST.get('date_of_birth').split('/')[::-1]
        # birthday[1], birthday[2] = birthday[2], birthday[1]
        # birthday = '-'.join(birthday)
        
        student = Student.objects.create(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            student_user_id = request.POST.get('username'),
            date_of_birth = request.POST.get('date_of_birth'),
            age = request.POST.get('age'),
            gender = request.POST.get('gender'),
            phone_number = request.POST.get('phone_number'),
            email = request.POST.get('email'),
            address = request.POST.get('address'),
            class_room = request.POST.get('class_room'),
            stu_no = request.POST.get('stu_no'),
            track = request.POST.get('track'),
            parent_id = Parent.objects.get(pk=request.POST.get('parent')),
            # teacher_id = Teacher.objects.get(pk=request.POST.get('teacher')),
            user=user
        )
       
        
        msg = 'SUCCESSFULLY ADD NEW STUDENT - NAME : %s' % (student.first_name)
    else:
        student = Student.objects.none()
    context = {
        'student': student,
        'parent':parent,
        'teacher':teacher,
        'gender': Student.GENDERS,
        'msg': msg
    }

    return render(request, 'student/student_add.html', context=context)

def student_detail(request, student_id):
   
    student = Student.objects.get(pk=student_id)
    return render(request, 'student/studentdetail.html', context={
        'student': student
        
    })

def student_update(request, student_id):
     
    try:
        student = Student.objects.get(pk=student_id)
        msg = ''
        parent = Parent.objects.all()
    except student.DoesNotExist: 
        return redirect('index')

    if request.method == 'POST':
        # birthday = request.POST.get('date_of_birth').split('/')[::-1]
        # birthday[1], birthday[2] = birthday[2], birthday[1]
        # birthday = '-'.join(birthday)
        student.first_name=request.POST.get('first_name')
        student.last_name=request.POST.get('last_name')
        # student.student_user_id=request.POST.get('username')
        student.date_of_birth=request.POST.get('date_of_birth')
        student.age=request.POST.get('age')
        student.gender=request.POST.get('gender')
        student.phone_number=request.POST.get('phone_number')
        student.email=request.POST.get('email')
        student.address=request.POST.get('address')
        student.class_room=request.POST.get('class_room')
        student.track=request.POST.get('track')
        student.parent_id=Parent.objects.get(pk=request.POST.get('parent'))
        # student.teacher_id = Teacher.objects.get(pk=request.POST.get('teacher'))
        
        student.save()
        msg = 'SUCCESSFULLY UPDATE STUDENT NAME : %s' % (student.first_name)
    

    return render(request, 'student/student_update.html', context={
        'student': student, 
        'gender': Student.GENDERS,
        'msg': msg,
        'parent':parent,
    })

def student_delete(request, student_id):
    
    student = Student.objects.get(id = student_id)
    student.delete()
    return redirect(to='index')

def teacher(request):

    
    teacher = Teacher.objects.all()
    
    return render(request, template_name='teacher/teacher.html', context={
        'teacher' : teacher
    })

def teacher_add(request):

    
    teacher = Teacher.objects.all()
    msg = ''
    if request.method == 'POST':
        user = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'),
            '1234'
        )
        group = Group.objects.get(name='teacher')
        user.groups.add(group)
        user.save()
        teacher = Teacher.objects.create(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            phone_number = request.POST.get('phone_number'),
            email = request.POST.get('email'),
            room = request.POST.get('room'),
            teacher_user_id = request.POST.get('username'),
            user=user
            
        )
        msg = 'SUCCESSFULLY CREATE NEW TEACHER NAME : %s' % (teacher.first_name)
    else:
        
        teacher = Teacher.objects.none()
    context = {
        'teacher' : teacher,
        'msg': msg
    }

    return render(request, 'teacher/teacher_add.html', context=context)

def teacher_update(request, teacher_id):

    try:
        teacher = Teacher.objects.get(pk=teacher_id)
       
        msg = ''
    except teacher.DoesNotExist: 
        return redirect('index')

    if request.method == 'POST':
        teacher.first_name=request.POST.get('first_name')
        teacher.last_name=request.POST.get('last_name')
        teacher.room=request.POST.get('room')
        teacher.phone_number=request.POST.get('phone_number')
        teacher.email=request.POST.get('email')
 
        teacher.save()
        msg = 'SUCCESSFULLY UPDATE TEACHER NAME : %s' % (teacher.first_name)
    
    context = {
        'teacher': teacher,    
        'msg': msg
    }

    return render(request, 'teacher/teacher_update.html', context=context)

def teacher_delete(request, teacher_id):
    
    teacher = Teacher.objects.get(id = teacher_id)
    teacher.delete()
    return redirect(to='teacher')

def course(request):
    
    course = Course.objects.all()
    
    return render(request, template_name='course/course.html', context={
        'course' : course
    })


def course_add(request):
    
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course')
    else:
        form = CourseForm()
        
    return render(request, 'course/course_add.html', context={
        'form': form
    })

def course_update(request, course_id):

    try:
        course = Course.objects.get(pk=course_id)
       
        msg = ''
    except course.DoesNotExist: 
        return redirect('index')

    if request.method == 'POST':
        course.name=request.POST.get('name')
        course.course_id=request.POST.get('course_id')
        course.room=request.POST.get('room')
        course.capacity=request.POST.get('capacity')
        course.start_time=request.POST.get('start_time')
        course.end_time=request.POST.get('end_time')
        # course.teach_course=request.POST.get('teach_course')
        course.weekday=request.POST.get('weekday')
 
        course.save()
        msg = 'SUCCESSFULLY UPDATE COURSE SUBJECT : %s' % (course.name)
    
    context = {
        'course': course,    
        'msg': msg,
        'weekday': Course.WEEKDAYS,
    }

    return render(request, 'course/course_update.html', context=context)

# def course_update(request, course_id):

#     if request.method == 'POST':
       
#         course = Course.objects.get(pk=course_id)
#         form = CourseForm(instance=course)
#         if form.is_valid():
#             form.save()
#             return redirect('course')
#     else:
#         form = CourseForm()
        
#     return render(request, 'course/course_add.html', context={
#         'form': form
#     })

# def course_update(request, id): 
    
#     instance = get_object_or_404(Course, id=pk)
#     form = Course(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         return redirect('course')
#     return render(request, 'course/course_add.html', {'form': form}) 

def course_delete(request, course_id):
    
    course = Course.objects.get(id = course_id)
    course.delete()
    return redirect(to='course')