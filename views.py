from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ContactUs, Student, admins
from django.contrib import messages
import json
from django.http import JsonResponse
import re


def index(request):
    students = Student.objects.all() # get all students
    context2 = {
        'ss': students  # send students to html page
    }
    if request.method == 'POST':
        contact_us = ContactUs() # create new object from ContactUs model
        contact_us.Fname = request.POST.get('Fname', '')
        contact_us.Lname = request.POST.get('Lname', '')
        contact_us.email = request.POST.get('email', '')
        contact_us.subject = request.POST.get('subject', '')
        contact_us.save()
        return render(request, 'home_page.html', context2)
    return render(request, 'home_page.html', context2)


def index2(request):
    students = Student.objects.all()
    context2 = {
        'ss': students
    }
    if request.method == 'POST':
        contact_us = ContactUs()
        contact_us.Fname = request.POST.get('Fname', '')
        contact_us.Lname = request.POST.get('Lname', '')
        contact_us.email = request.POST.get('email', '')
        contact_us.subject = request.POST.get('subject', '')
        contact_us.save()
        return render(request, 'home_page2.html', context2)
    return render(request, 'home_page2.html', context2)


def addStudent(request):
    if request.method == 'POST':
        # Retrieve form data
        student_id = request.POST.get('id')
        name = request.POST.get('name')
        level = request.POST.get('lvl')
        department = request.POST.get('DB')
        status = request.POST.get('status')
        email = request.POST.get('mail')
        gender = request.POST.get('gender')
        phone = request.POST.get('tele')
        birth_date = request.POST.get('date')
        GPA = request.POST.get('gpa')

        # Regular expression patterns
        id_pattern = r'^\d{8}$'  # 8-digit ID pattern
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Email pattern
        phone_pattern = r'^\d{11}$'  # 11-digit phone number pattern

        # Validate ID
        if not re.match(id_pattern, student_id):
            messages.error(request, 'Invalid ID. It should be 8 numbers.')
            return redirect('addStudent')

        # Validate Email
        if not re.match(email_pattern, email):
            messages.error(request, 'Invalid email address.')
            return redirect('addStudent')

        # Validate Phone Number
        if not re.match(phone_pattern, phone):
            messages.error(request, 'Invalid phone number. It should be 11 numbers.')
            return redirect('addStudent')

        # Check if the student ID already exists
        existing_students = Student.objects.filter(student_id=student_id)
        if existing_students.exists():
            messages.error(request, 'The student ID already exists.')
            return redirect('addStudent')

        if student_id:
            if int(level) >= 3:
                student = Student(
                    student_id=student_id, name=name, level=level, department=department,
                    status=status, email=email, gender=gender, phone=phone, birth_date=birth_date, GPA=GPA)
                student.save()
                messages.info(request, 'The student data is set successfully.')
                return render(request, 'addStudent.html')
            else:
                student = Student(
                    student_id=student_id, name=name, level=level, department='general',
                    status=status, email=email, gender=gender, phone=phone, birth_date=birth_date, GPA=GPA)
                student.save()
                messages.info(request, 'The student data is set successfully.')
                return render(request, 'addStudent.html')
        else:
            messages.error(request, 'Invalid student ID or gender provided.')
            return redirect('addStudent')

    return render(request, 'addStudent.html')


def updateStudent(request):
    return render(request, 'edit_page.html')


def logout(request):
    return render(request, 'home_page.html')


def active(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'active_students.html', context)


def update_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student_id = data.get('student_id')
        status = data.get('status')
        if student_id and status:
            try:
                student = Student.objects.get(student_id=student_id)
                student.status = status
                student.save()
                return HttpResponse('Status updated successfully')
            except Student.DoesNotExist:
                return HttpResponse('Student not found', status=404)
        else:
            return HttpResponse('Invalid parameters', status=400)
    else:
        return HttpResponse('Invalid request method', status=405)


def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        admin = admins.objects.filter(email=email, password=password)
        if admin:
            return redirect('home2')
        else:
            messages.error(request, 'Invalid Email or Password')
            return redirect('loginForm')

    return render(request, 'sign_in.html')



def register(request):
    if request.method == 'POST':
        userName = request.POST.get('userName')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        verifyPassword = request.POST.get('verifyPassword')

        # Validate email format using regex
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            messages.error(request, 'Invalid email address')
            return redirect('registerForm')

        # Validate password format using regex
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password1):
            messages.error(request, 'Weak password')
            return redirect('registerForm')

        if password1 == verifyPassword:
            if admins.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('registerForm')
            admin = admins(userName=userName, email=email, password=password1, verifyPassword=verifyPassword)
            admin.save()
            return redirect('signin')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('registerForm')

    return render(request, 'register.html')



def signin(request):
    return render(request, 'sign_in.html')


def home_page2(request):
    return render(request, 'home_page2.html')


def newPassword(request):
    if request.method == 'POST':
        password1 = request.POST.get('password')
        verifyPassword = request.POST.get('verifyPassword')

        # Validate password format using regex
        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password1):
            messages.error(request, 'Password must contain at least 8 characters,1 lowercase,1 uppercase,1 digit,1 special character')
            return redirect('newPassword')

        if password1 == verifyPassword:
            admin = admins.objects.filter(email=email).first()
            if admin:
                admin.password = password1
                admin.verifyPassword = verifyPassword
                admin.save()
                return redirect('loginForm')
            else:
                return redirect('newPassword')
        else:
            messages.error(request, 'Passwords doesn\'t match')
            return redirect('newPassword')

    return render(request, 'NewPass.html')

def forget_password(request):
    if request.method == 'POST':
        global email
        email = request.POST.get('email')
        if admins.objects.filter(email=email).exists():
            return redirect('newPassword')

        else:
            messages.error(request, 'Email not found')
            return redirect('forget')

    return render(request, 'forgot_password.html')


def delete_student(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            # Get the student ID from the form
            student_id = request.POST.get('id')
            name = request.POST.get('username')

            try:
                student = Student.objects.get(student_id=student_id, name=name)
                student.delete()
                messages.success(request, 'Student deleted successfully.')

            except Student.DoesNotExist:
                messages.error(request, 'Student not found.')

            return redirect('delete')

    return render(request, 'delete.html')

def edit_page_view(request):
    if request.method == 'POST':
        student_id = request.POST.get('id')

        try:
            # Retrieve the student from the database
            student = Student.objects.get(student_id=student_id)
            student.name = request.POST.get('username')
            student.email = request.POST.get('email')
            student.phone = request.POST.get('phone')
            student.birth_date = request.POST.get('date')
            student.GPA = request.POST.get('gpa')
            status = request.POST.get('status')

            if status == 'on':
                student.status = 'Active'
            else:
                student.status = 'Inactive'

            student.save()
            messages.success(request, 'Student updated successfully.')
        except Student.DoesNotExist:
            messages.error(request, 'Student not found.')
        return redirect('edit_page_view')

    else:
        # Render the edit page template
        return render(request, 'edit_page.html')


def search_page(request):
    return render(request, 'search_student.html')


def search_student(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        print(f"Received student name: {student_name}")
        if len(student_name) != 0:
            students = Student.objects.filter(name__icontains=student_name.strip(), status="Active").order_by(
                'student_id')
            serialized_students = serializers.serialize('json', students)
        else:
            serialized_students = []
        data = {
            'students': serialized_students
        }
        return JsonResponse(data, safe=False)
    else:
        return render(request, 'search_student.html')


def assign_department(request):
    return render(request, 'avaliable_departments.html')


def search_student_id(request):
    if request.method == "POST":
        entered_id = request.POST.get("student_id")
        if entered_id and entered_id.isdigit():
            student = Student.objects.filter(student_id=entered_id.strip())
            serialized_student = serializers.serialize('json', student)
        else:
            serialized_student = "{}"
        return JsonResponse(serialized_student, safe=False)


def assign_to_student(request):
    if request.method == "POST":
        entered_id = request.POST.get("student_id")
        selectedDepartment = request.POST.get("department")
        print(f"Received selected department: {selectedDepartment}")
        if entered_id and selectedDepartment:
            student = get_object_or_404(Student, student_id=entered_id)
            student.department = selectedDepartment
            student.save()
            serialized_student = serializers.serialize('json', [student])
            return JsonResponse(serialized_student, safe=False)
